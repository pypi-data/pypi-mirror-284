from promptflow import tool
import urllib.request
import json
import os
import ssl


@tool
def get_recommendation_intelligence_flow_api(
    allowed, chat_input, end_point, api_key, deployment_name
):
    allowed = True

    if (
        allowed
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context

        data = {"chat_input": chat_input}
        body = json.dumps(data).encode("utf-8")

        url = end_point
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")

        # The azureml-model-deployment header will force the request to go to a specific deployment.
        # Remove this header to have the request observe the endpoint traffic rules
        headers = {
            "Content-Type": "application/json",
            "Authorization": ("Bearer " + api_key),
            "azureml-model-deployment": deployment_name,
        }

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            result = response.read()
            decoded_string = result.decode("utf-8")
            json_data = json.loads(decoded_string)
            chat_output = json_data.get("chat_output", "")

            final_output = {"chat_output": chat_output}
            final_output_str = json.dumps(final_output, ensure_ascii=False, indent=4)

            return final_output_str
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(error.read().decode("utf8", "ignore"))
            return "The request failed with status code: " + str(error.code)
    return False
