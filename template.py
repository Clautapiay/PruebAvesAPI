from consumir_api import request_json
from string import Template

url = "https://aves.ninjas.cl/api/birds"
response = request_json(url)

# print(response)
# for elemento in response:
    # print(elemento["images"]["main"]) #imprime todos los links de las imagenes "main"
    # print(elemento["name"]["spanish"])

lista_img = [(elemento["images"]["main"], elemento["name"]["english"], elemento["name"]["spanish"]) for elemento in response]
print(lista_img)

nuevo_card =  """<div class="card" style="width: 18rem;">
                <img src="$url" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">$name2</h5>
                    <h5 class="card-title">$name</h5>
                </div>
            </div>"""

# img_template = Template('<img src="$url">')
img_template = Template(nuevo_card)
texto_img = ''
# imagen = img_template.subtitute(url = "https://aves.ninjas.cl/api/site/assets/files/3698/19082018091938pato_colorado_macho_pedro_valencia_web.200x0.jpg")
for img, name, name2 in lista_img:
    texto_img += img_template.substitute(url = img, name = name, name2 = name2) + '\n'

# print(texto_img)

html_template = Template('''<!doctype html>
    <title>AvesChile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <link rel="stylesheet" href="assets/css/style.css">
  </head>
  <body class="bg-total">
    <h1 class="text-center">Aves De Chile</h1>
    <div class="container">
        <div class="row">
            <div class="card>
            <h5 class="card-title"></h5>
            <h5 class="card-title"></h5>
            </div>
           $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body = texto_img)
# print(html)

archivo = open('index.html', 'w+', encoding='utf-8')
archivo.write(html)
archivo.close()

