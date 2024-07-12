import requests


class AuctionClient:
    """
    법원경매 클라이언트
    https://www.courtauction.go.kr/
    """
    def __init__(self):
        pass

    def get_item_list(self,
                      daepyo_sido_cd,
                      term_start_dt,
                      term_end_dt,
                      lcls_util_cd,
                      mcls_util_cd,
                      scls_util_cd,
                      target_row,
                      page_spec):
        """
        물건상세검색 메뉴
        """
        url = "https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf"
        data = {
            "daepyoSidoCd": daepyo_sido_cd,
            "termStartDt": term_start_dt,
            "termEndDt": term_end_dt,
            "lclsUtilCd": "",
            "mclsUtilCd": "",
            "sclsUtilCd": "",
            "targetRow": target_row,
            "page": page_spec,
            "pageSpec": page_spec,

            "bubwLocGubun": "2",
            "realVowel": "35207_45207",
            "ipchalGbncd": "000331",
            "mvRealGbncd": "00031R",
            "srnID": "PNO102001",
            "_SRCH_SRNID": "PNO102001",
            "_CUR_CMD": "InitMulSrch.laf",
            "_CUR_SRNID": "PNO102001",
            # "_NEXT_CMD": "RetrieveRealEstMulDetailList.laf",
            "_NEXT_SRNID": "PNO102002",
            "_FORM_YN": "Y"
        }

        response = requests.post(url, data=data)
        return response.text



client = AuctionClient()
item_list = client.get_item_list(
    daepyo_sido_cd="11",
    term_start_dt="2024.07.12",
    term_end_dt="2024.07.26",
    lcls_util_cd="0000802",
    mcls_util_cd="000080201",
    scls_util_cd="00008020106",
    target_row="91",
    page_spec="default10"
)

print(item_list)