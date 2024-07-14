import ofscraper.classes.sessionmanager.ofsession as ofsessionmanager
import ofscraper.classes.sessionmanager.sessionmanager as sessionManager
import ofscraper.download.utils.globals as common_globals
import ofscraper.utils.constants as constants
from ofscraper.download.utils.retries import get_download_req_retries


class download_session(sessionManager.sessionManager):
    def __init__(
        self, sem=None, retries=None, wait_min=None, wait_max=None, log=None
    ) -> None:
        sem = sem or common_globals.sem
        retries = retries or get_download_req_retries()
        wait_min = wait_min or constants.getattr("OF_MIN_WAIT_API")
        wait_max = wait_max or constants.getattr("OF_MAX_WAIT_API")
        log = log or common_globals.log
        super().__init__(
            sem=sem, retries=retries, wait_min=wait_min, wait_max=wait_max, log=log
        )


class cdm_session(sessionManager.sessionManager):
    def __init__(self, backend=None, sem=None) -> None:
        backend = backend or "httpx"
        sem = sem or common_globals.sem
        super().__init__(sem=sem, backend=backend)


class cdm_session_manual(ofsessionmanager.OFSessionManager):
    def __init__(self, backend=None, sem=None) -> None:
        backend = backend or "httpx"
        sem = sem or common_globals.sem
        super().__init__(sem=sem, backend=backend)
