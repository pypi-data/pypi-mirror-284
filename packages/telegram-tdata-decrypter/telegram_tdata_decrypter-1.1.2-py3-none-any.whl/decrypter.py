import os
import hashlib

from typing import Tuple, List, Dict

from io import BytesIO

from qt import read_qt_int32, read_qt_uint64
from file_io import read_tdf_file, read_encrypted_file
from settings import SettingsBlocks, read_settings_blocks
from storage import decrypt_key_data_tdf, read_key_data_accounts, decrypt_settings_tdf


def file_to_to_str(filekey: bytes):
    return ''.join(f'{b:X}'[::-1] for b in filekey)


def compute_data_name_key(dataname: str):
    filekey = hashlib.md5(dataname.encode('utf8')).digest()[:8]
    return file_to_to_str(filekey)


def compose_account_name(dataname: str, index: int):
    if index > 0:
        return f'{dataname}#{index+1}'
    else:
        return dataname


class ParsedAccount:
    def __init__(self):
        self.index: int = None
        self.mtp_data: MtpData = None

    def __repr__(self):
        return f'ParsedAccount(index={self.index})'


class MtpData:
    def __init__(self):
        self.user_id: int = None
        self.current_dc_id: int = None
        self.keys: Dict[int, bytes] = None
        self.keys_to_destroy: Dict[int, bytes] = None

    def __repr__(self):
        return f'MtpData(user_id={self.user_id})'


def read_mtp_authorization(data: BytesIO) -> MtpData:
    legacy_user_id = read_qt_int32(data)
    legacy_main_dc_id = read_qt_int32(data)

    if legacy_user_id == -1 and legacy_main_dc_id == -1:
        user_id = read_qt_uint64(data)
        main_dc_id = read_qt_int32(data)
    else:
        user_id = legacy_user_id
        main_dc_id = legacy_main_dc_id

    def read_keys():
        count = read_qt_int32(data)

        return {
            read_qt_int32(data): data.read(256)
            for _ in range(count)
        }

    mtp_data = MtpData()
    mtp_data.user_id = user_id
    mtp_data.current_dc_id = main_dc_id
    mtp_data.keys = read_keys()
    mtp_data.keys_to_destroy = read_keys()
    return mtp_data


class AccountReader:
    def __init__(self, base_path: str, index: int, dataname: str = None):
        self._base_path = base_path
        self._index = index
        self._account_name = compose_account_name(dataname, index)
        self._dataname_key = compute_data_name_key(self._account_name)

    def read(self, local_key: bytes) -> ParsedAccount:
        parsed_account = ParsedAccount()
        parsed_account.index = self._index
        parsed_account.mtp_data = self.read_mtp_data(local_key)
        return parsed_account

    def read_mtp_data(self, local_key: bytes) -> MtpData:
        mtp_data_file_path = os.path.join(self._base_path, self._dataname_key)
        version, mtp_data_settings = read_encrypted_file(mtp_data_file_path, local_key)
        blocks = read_settings_blocks(version, BytesIO(mtp_data_settings))
        mtp_authorization = blocks[SettingsBlocks.dbiMtpAuthorization]
        return read_mtp_authorization(BytesIO(mtp_authorization))


class ParsedTdata:
    def __init__(self):
        self.settings = None
        self.accounts: Dict[int, ParsedAccount] = None


class TdataReader:
    DEFAULT_DATANAME = 'data'

    def __init__(self, base_path: str, dataname: str = None):
        self._base_path = base_path
        self._dataname = dataname or TdataReader.DEFAULT_DATANAME

    def read(self, passcode: str = None) -> ParsedTdata:
        parsed_tdata = ParsedTdata()
        parsed_tdata.settings = self.read_settings()

        local_key, account_indexes = self.read_key_data(passcode)

        accounts = {}

        for account_index in account_indexes:
            account_reader = AccountReader(self._base_path, account_index, self._dataname)
            accounts[account_index] = account_reader.read(local_key)

        parsed_tdata.accounts = accounts
        return parsed_tdata

    def read_key_data(self, passcode: str = None) -> Tuple[bytes, List[int]]:
        if passcode is None:
            passcode = ''

        key_data_tdf = read_tdf_file(self._path(self._key_data_name()))
        local_key, account_indexes_data = decrypt_key_data_tdf(passcode.encode(), key_data_tdf)
        account_indexes, _ = read_key_data_accounts(BytesIO(account_indexes_data))

        return local_key, account_indexes

    def read_settings(self):
        settings_tdf = read_tdf_file(self._path('settings'))
        settings_decrypted = decrypt_settings_tdf(settings_tdf)
        return read_settings_blocks(settings_tdf.version, BytesIO(settings_decrypted))

    def _path(self, child: str) -> str:
        return os.path.join(self._base_path, child)

    def _key_data_name(self):
        return 'key_' + self._dataname
