from moriarty.sidecar.params import InferenceProxyStatus, MatrixCallback


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200


def test_callback(client, inference_log):
    response = client.post(
        "/callback",
        data=MatrixCallback(
            inference_id=inference_log,
            status=InferenceProxyStatus.FINISHED,
            msg=f"Inference {inference_log} finished",
            payload="{}",
        ).model_dump_json(),
    )
    assert response.status_code == 200
