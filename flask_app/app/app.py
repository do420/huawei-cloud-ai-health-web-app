from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from PIL import Image
from functions import get_xauth

app = Flask(__name__)

# M->N
x_auth_code = get_xauth() # or """YOUR_XAUTH_TOKEN"""

result_text = ""
uploaded_image_path = "static/uploaded_img.jpeg"

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/predict-pneumonia-xray', methods=['POST', 'GET'])
def predict_pneumonia():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"


    x_auth = x_auth_code
    # Making a request to the Huawei Cloud ModelArts API
    api_url = 'your_api_url' # 'https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/f21d0fcb-2a99-4fff-9f53-5dbab8272e79'

    headers = {'X-Auth-Token': x_auth}


    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)
                result_text += "%" + str(score * 100) + " ihtimalle " + label+". "
                # Convert the score to a float
                score = float(score)
                additional_text = ""
                if predicted_label == "pneumonia":
                    if (score*100) < 75:
                        additional_text = "Doktora görünseniz iyi olur."
                    else:
                        additional_text = "Acilen doktora görünmelisiniz."


                    result_text += additional_text

                    break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))


@app.route('/predict-sars-cov-2-tomography', methods=['POST', 'GET'])
def predict_sars_cov_2():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    im_saved = image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"


    x_auth = x_auth_code
    # Making a request to the Huawei Cloud ModelArts API
    api_url = 'https://1c083ce4e2164344bac8cc686e0f509e.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/65717c20-a3fc-4b89-be17-5b6ba261ad10'

    headers = {'X-Auth-Token': x_auth}


    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)
                if label == "COVID":
                    result_text += "%" + str(score * 100) + " ihtimalle " + label.capitalize() + "."
                else:
                    result_text += "%" + str(score * 100) + " ihtimalle Covid değil."

                # Convert the score to a float
                score = float(score)
                additional_text = ""
                if predicted_label == "covid":
                    if (score*100) < 75:
                        additional_text = "Doktora görünseniz iyi olur."
                    else:
                        additional_text = "Acilen doktora görünmelisiniz."


                    result_text += additional_text

                    break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))

@app.route('/predict-alzheimer-mri', methods=['POST', 'GET'])
def predict_alzheimer_mri():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"


    x_auth =  x_auth_code
    #Huawei Cloud ModelArts API
    api_url = 'https://2fec676ce4e447d0980abfbeb404b0a3.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/37dabbcc-9508-4d1e-949e-aaae863c7a81'

    headers = {'X-Auth-Token': x_auth}


    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)
                if label == "MildDemented":

                    result_text += "%" + str(score * 100) + " ihtimalle hafif derece Demans."
                elif label == "ModerateDemanted":

                    result_text += "%" + str(score * 100) + " ihtimalle orta derece Demans."
                elif label == "NonDemented":

                    result_text += "%" + str(score * 100) + " ihtimalle Demans bulunamadı."
                elif label == "VeryMildDemented":

                    result_text += "%" + str(score * 100) + " ihtimalle çok az derece Demans."






                break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))

@app.route('/predict-brain-tumor-mri', methods=['POST', 'GET'])
def predict_brain_tumor_mri():
    file = request.files['file']
    global x_auth_code
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"

    x_auth = x_auth_code
    # Making a request to the Huawei Cloud ModelArts API
    api_url = 'https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/759e67cb-940c-45d2-95d8-7168f2540e9d'

    headers = {'X-Auth-Token': x_auth}


    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)

                if label == "glioma_tumor":

                    result_text += "%" + str(score * 100) + " ihtimalle Glioma tümörü mevcuttur."
                elif label == "no_tumor":

                    result_text += "%" + str(score * 100) + " ihtimalle herhangi bir tümör mevcut değildir."
                elif label == "meningioma_tumor":

                    result_text += "%" + str(score * 100) + " ihtimalle Glioma tümörü mevcuttur."
                elif label == "pituitary_tumor":

                    result_text += "%" + str(score * 100) + " ihtimalle Pituitary tümörü mevcuttur."

                break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))

@app.route('/predict-blood-cell-micro', methods=['POST', 'GET'])
def predict_blood_cell_micro():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"


    x_auth = x_auth_code
    #to the Huawei Cloud ModelArts API
    api_url = 'https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/31c96886-6656-4d08-9db5-333f7a08d406'

    headers = {'X-Auth-Token': x_auth}


    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)
                if label == "0-":

                    result_text += "%" + str(score * 100) + " ihtimalle Nötrofil örneğidir."
                elif label == "1-":

                    result_text += "%" + str(score * 100) + " ihtimalle Eozinofil polimorf örneğidir."
                elif label == "2-":

                    result_text += "%" + str(score * 100) + " ihtimalle Bazofil örneğidir."
                elif label == "3-":

                    result_text += "%" + str(score * 100) + " ihtimalle Lenfosit örneğidir."
                elif label == "4-":

                    result_text += "%" + str(score * 100) + " ihtimalle Monosit örneğidir."
                elif label == "5-":

                    result_text += "%" + str(score * 100) + " ihtimalle Gronülosit örneğidir."
                elif label == "6-":

                    result_text += "%" + str(score * 100) + " ihtimalle Eritroblast örneğidir."
                elif label == "7-":

                    result_text += "%" + str(score * 100) + " ihtimalle Trombosit örneğidir."

                break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))


@app.route('/predict-breast-cancer-ultrason', methods=['POST', 'GET']) #meme kanseri için ultrason
def predict_breast_cancer_ultrason():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"


    x_auth =  x_auth_code
    # Making a request to the Huawei Cloud ModelArts API
    api_url = 'https://1c083ce4e2164344bac8cc686e0f509e.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/afe465c8-bf65-4d6a-abc0-386215c7c00e'

    headers = {'X-Auth-Token': x_auth}


    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)

                if label == "negative":

                    result_text += "%" + str(score * 100) + " ihtimalle kötü huylu hücreye rastlanılmıştır."
                elif label == "positive":

                    result_text += "%" + str(score * 100) + " ihtimalle kötü huylu hücreye rastlanılmamıştır."

                break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))

@app.route('/predict-choroidal-neovascularization', methods=['POST', 'GET'])
def predict_choroidal_neovascularization():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"

    x_auth = x_auth_code
    # Making a request to the Huawei Cloud ModelArts API
    api_url = 'https://2fec676ce4e447d0980abfbeb404b0a3.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/c7907d21-0047-4c87-ab46-f680763d9101'

    headers = {'X-Auth-Token': x_auth}
    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)
                if label == "0-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Koroid neovaskülarizasyon' örneğidir."
                elif label == "1-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'diyabetik maküler ödem' örneğidir."
                elif label == "2-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Drusen' örneğidir."
                elif label == "3-":

                    result_text += "%" + str(score * 100) + " ihtimalle normal göz örneğidir."

                break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))

@app.route('/predict-derma-base', methods=['POST', 'GET'])
def predict_derma_base():
    file = request.files['file']
    global result_text
    # Assuming the file is an image, you can use PIL to open it
    image = Image.open(file)
    image.save("app/static/uploaded_img.jpeg")
    global uploaded_image_path
    uploaded_image_path = "static/uploaded_img.jpeg"

    x_auth = x_auth_code
    # Making a request to the Huawei Cloud ModelArts API
    api_url = "https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/0969549c-90c0-4f34-8ba2-02642155f749"

    headers = {'X-Auth-Token': x_auth}
    payload = {}

    files = [
        ('images', ('uploaded_img.jpeg', open(
            'app/static/uploaded_img.jpeg',
            'rb'), 'image/jpeg'))
    ]

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)

    result = response.text

    print(result)

    if "error_msg" not in result:
        json_data = json.loads(result)
        predicted_label = json_data['predicted_label']
        result_text = "Yapay zeka modelinin tahmini: "
        # Find the entry for the predicted label in the 'scores' list
        for label, score in json_data['scores']:
            if label == predicted_label:
                score = float(score)
                score = round(score, 2)
                if label == "0-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Aktinik keratoz' örneğidir."
                elif label == "1-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Bazal hücreli karsinom' örneğidir."
                elif label == "2-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'liken planus veya Seboreik keratoz' örneğidir."
                elif label == "3-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Dermatofibrom' örneğidir."
                elif label == "4-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Melanom' örneğidir."

                elif label == "5-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'Melanotik nevus' örneğidir."
                elif label == "6-":

                    result_text += "%" + str(score * 100) + " ihtimalle 'damar lezyonu' örneğidir."


                break

    # Pass the dynamic parameters directly to the 'results' route
    return redirect(url_for('results'))


@app.route('/results')
def results(dynamic_text = result_text, img_path = uploaded_image_path):
    return render_template('result.html', dynamic_text=result_text, img_path=uploaded_image_path)






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
