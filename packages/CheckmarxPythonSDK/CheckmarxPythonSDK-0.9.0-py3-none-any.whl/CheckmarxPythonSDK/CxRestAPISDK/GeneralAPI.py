# encoding: utf-8
import json

from .httpRequests import get_request, post_request, patch_request, delete_request, get_headers
from CheckmarxPythonSDK.utilities.compat import OK, CREATED, NO_CONTENT, ACCEPTED
from .sast.general.dto import CxServerLicenseData, CxSupportedLanguage, CxTranslationInput


class GeneralAPI:
    """
    CxSAST general API
    """

    @staticmethod
    def get_server_license_data(api_version="4.0"):
        """
        Returns the CxSAST server's license data
        """
        result = None
        relative_url = "/cxrestapi/serverLicenseData"
        response = get_request(relative_url=relative_url, headers=get_headers(api_version))
        if response.status_code == OK:
            json = response.json()
            result = CxServerLicenseData(
                current_audit_users=json["currentAuditUsers"],
                current_projects_count=json["currentProjectsCount"],
                current_users=json["currentUsers"],
                edition=json["edition"],
                expiration_date=json["expirationDate"],
                hid=json["hid"],
                is_osa_enabled=json["isOsaEnabled"],
                max_audit_users=json["maxAuditUsers"],
                max_concurrent_scans=json["maxConcurrentScans"],
                max_loc=json["maxLOC"],
                max_users=json["maxUsers"],
                osa_expiration_date=json["osaExpirationDate"],
                projects_allowed=json["projectsAllowed"],
                supported_languages=[
                    CxSupportedLanguage(
                        is_supported=item["isSupported"],
                        language=item["language"])
                    for item in json["supportedLanguages"]
                ]
            )
        return result

    @staticmethod
    def get_server_system_version(api_version="1.1"):
        """
        Returns version, hotfix number and engine pack version
        Returns:
            {
              "version": "string",
              "hotFix": "string",
              "enginePackVersion": "string"
            }
        """
        result = None
        relative_url = "/cxrestapi/system/version"
        response = get_request(relative_url=relative_url, headers=get_headers(api_version))
        if response.status_code == OK:
            result = response.json()
        return result

    @staticmethod
    def get_result_states(api_version="4.0"):
        """

        Args:
            api_version:

        Returns:

        """
        """
        [
          {
            "id": 0,
            "names": [
              {
                "languageId": 1028,
                "name": "校驗",
                "isConstant": true
              },
              {
                "languageId": 1033,
                "name": "To Verify",
                "isConstant": true
              },
              {
                "languageId": 1034,
                "name": "Para verificar",
                "isConstant": true
              },
              {
                "languageId": 1036,
                "name": "Pour vérifier",
                "isConstant": true
              },
              {
                "languageId": 1041,
                "name": "確認必要",
                "isConstant": true
              },
              {
                "languageId": 1042,
                "name": "확인하려면",
                "isConstant": true
              },
              {
                "languageId": 1046,
                "name": "Verificar",
                "isConstant": true
              },
              {
                "languageId": 1049,
                "name": "Проверять",
                "isConstant": true
              },
              {
                "languageId": 2052,
                "name": "等待确认",
                "isConstant": true
              }
            ],
            "permission": "set-result-state-toverify"
          },
          {
            "id": 1,
            "names": [
              {
                "languageId": 1028,
                "name": "不可利用",
                "isConstant": true
              },
              {
                "languageId": 1033,
                "name": "Not Exploitable",
                "isConstant": true
              },
              {
                "languageId": 1034,
                "name": "No explotable",
                "isConstant": true
              },
              {
                "languageId": 1036,
                "name": "Non exploitable",
                "isConstant": true
              },
              {
                "languageId": 1041,
                "name": "悪用はできない",
                "isConstant": true
              },
              {
                "languageId": 1042,
                "name": "악용할 수 없음",
                "isConstant": true
              },
              {
                "languageId": 1046,
                "name": "Não Exploitável",
                "isConstant": true
              },
              {
                "languageId": 1049,
                "name": "Не эксплуатируемый",
                "isConstant": true
              },
              {
                "languageId": 2052,
                "name": "不可利用",
                "isConstant": true
              }
            ],
            "permission": "set-result-state-notexploitable"
          },
          {
            "id": 2,
            "names": [
              {
                "languageId": 1028,
                "name": "確認",
                "isConstant": false
              },
              {
                "languageId": 1033,
                "name": "Confirmed",
                "isConstant": false
              },
              {
                "languageId": 1034,
                "name": "Confirmado",
                "isConstant": false
              },
              {
                "languageId": 1036,
                "name": "Confirmé",
                "isConstant": false
              },
              {
                "languageId": 1041,
                "name": "確認済み",
                "isConstant": false
              },
              {
                "languageId": 1042,
                "name": "확인됨",
                "isConstant": false
              },
              {
                "languageId": 1046,
                "name": "Confirmado",
                "isConstant": false
              },
              {
                "languageId": 1049,
                "name": "Подтвердил",
                "isConstant": false
              },
              {
                "languageId": 2052,
                "name": "已确认",
                "isConstant": false
              }
            ],
            "permission": "set-result-state-confirmed"
          },
          {
            "id": 3,
            "names": [
              {
                "languageId": 1028,
                "name": "緊急",
                "isConstant": false
              },
              {
                "languageId": 1033,
                "name": "Urgent",
                "isConstant": false
              },
              {
                "languageId": 1034,
                "name": "Urgente",
                "isConstant": false
              },
              {
                "languageId": 1036,
                "name": "Urgent",
                "isConstant": false
              },
              {
                "languageId": 1041,
                "name": "緊急",
                "isConstant": false
              },
              {
                "languageId": 1042,
                "name": "긴급",
                "isConstant": false
              },
              {
                "languageId": 1046,
                "name": "Urgente",
                "isConstant": false
              },
              {
                "languageId": 1049,
                "name": "Срочный",
                "isConstant": false
              },
              {
                "languageId": 2052,
                "name": "紧急",
                "isConstant": false
              }
            ],
            "permission": "set-result-state-urgent"
          },
          {
            "id": 4,
            "names": [
              {
                "languageId": 1028,
                "name": "推薦不可用",
                "isConstant": true
              },
              {
                "languageId": 1033,
                "name": "Proposed Not Exploitable",
                "isConstant": true
              },
              {
                "languageId": 1034,
                "name": "Propuesto no explotable",
                "isConstant": true
              },
              {
                "languageId": 1036,
                "name": "Proposition non exploitable",
                "isConstant": true
              },
              {
                "languageId": 1041,
                "name": "悪用不可を提案",
                "isConstant": true
              },
              {
                "languageId": 1042,
                "name": "수용 할 수 없는 제안",
                "isConstant": true
              },
              {
                "languageId": 1046,
                "name": "Proposta Não Exploitável",
                "isConstant": true
              },
              {
                "languageId": 1049,
                "name": "Предлагается не использовать",
                "isConstant": true
              },
              {
                "languageId": 2052,
                "name": "提议不可利用",
                "isConstant": true
              }
            ],
            "permission": "set-result-state-proposednotexploitable"
          }
        ]
"""
        result = None
        relative_url = "/cxrestapi/sast/resultStates"
        response = get_request(relative_url=relative_url, headers=get_headers(api_version))
        if response.status_code == OK:
            result = response.json()
        return result

    @staticmethod
    def create_result_state(translation_inputs, permission, api_version="4.0"):
        """

        Args:
            translation_inputs (List of `CxTranslationInput`):
            permission (str): example, "set-result-state-toverify"
            api_version (str):

        Returns:
            Id of result state(int)
        """
        result = None
        if not isinstance(translation_inputs, (list, tuple)):
            raise ValueError("translation_inputs should be list or tuple")
        for item in translation_inputs:
            if not isinstance(item, CxTranslationInput):
                raise ValueError("member of translation_inputs should be CxTranslationInput")

        result = None
        post_data = json.dumps(
            {
                "names": [item.to_dict() for item in translation_inputs],
                "permission": permission
            }
        )
        relative_url = "/cxrestapi/sast/resultStates"
        response = post_request(relative_url=relative_url, data=post_data, headers=get_headers(api_version))
        if response.status_code == OK:
            result = response.json().get("id")
        return result

    @staticmethod
    def update_result_state(state_id, translation_inputs, permission, api_version="4.0"):
        """

        Args:
            state_id (int):
            translation_inputs (List of `CxTranslationInput`):
            permission (str): example, "set-result-state-toverify"
            api_version (str):

        Returns:
            bool
        """
        is_successful = False
        if not isinstance(translation_inputs, (list, tuple)):
            raise ValueError("translation_inputs should be list or tuple")
        for item in translation_inputs:
            if not isinstance(item, CxTranslationInput):
                raise ValueError("member of translation_inputs should be CxTranslationInput")
        patch_data = json.dumps(
            {
                "names": [item.to_dict() for item in translation_inputs],
                "permission": permission
            }
        )
        relative_url = "/cxrestapi/sast/resultStates/{id}".format(id=state_id)
        response = patch_request(relative_url=relative_url, data=patch_data, headers=get_headers(api_version))
        if response.status_code == NO_CONTENT:
            is_successful = True
        return is_successful

    @staticmethod
    def delete_result_state(state_id, api_version="4.0"):
        """

        Args:
            state_id (int): The Id of the Result State
            api_version (str):
        Returns:
            bool
        """
        is_successful = False
        relative_url = "/cxrestapi/sast/resultStates/{id}".format(id=state_id)
        response = delete_request(relative_url=relative_url, headers=get_headers(api_version))
        if response.status_code == ACCEPTED:
            is_successful = True
        return is_successful

