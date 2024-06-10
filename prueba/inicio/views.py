from django.shortcuts import render,HttpResponse


def principal(request):
    return render(request,"inicio/principal.html")

def contacto(request):
    return render(request,"inicio/contacto.html")

def formulario(request):
    contenido="""<h2>Registrar</h2>
    <p>Matricula: <input type:"text" name="matricula"></p>
    <p>Nombre: <input type:"text" name="nombre"></p>
    <p>Carrera:
        <select>
            <option>ING. DSG</option>
            <option>ING. EVND</option>
        </select>
    </p>
    <input type="radio" name="turno" values="matutino">Matutino
    <input type="radio" name="turno" values="vespertino">Vespertino
    <p><input type="Button" name="enviar" value="Enviar"></p>
    """
    return HttpResponse(contenido)