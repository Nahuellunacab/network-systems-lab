# Docker Network Lab — Comunicación entre contenedores

## 🎯 Objetivo

Analizar cómo se comunican múltiples servicios dentro de una red interna utilizando Docker.

---

## 🧱 Arquitectura

[ client container ] → [ api container ]

---

## ⚙️ Tecnologías

* Docker
* Docker Compose
* FastAPI
* Python requests

---

## 🚀 Implementación

Se crearon dos servicios:

### API

* Servidor FastAPI escuchando en puerto 8000

### Client

* Script en Python que realiza requests periódicas a la API

---

## 🧪 Pruebas realizadas

### 🔹 Comunicación entre contenedores

El cliente realiza requests a:

http://api:8000

Resultado:

* Respuestas HTTP 200 OK
* Comunicación exitosa entre contenedores

   ![Comunicación entre contenedores](../images/comunicacion_contenedores.png)

* logs mostrando responses

---

### 🔹 Inspección de red

Se utilizó:

```bash
docker network inspect
```

Resultado:

* Cada contenedor tiene una IP interna
* Ambos están en la misma red
    ![Listado de redes](../images/network_ls.png)

   ![Inspección de red](../images/network_inspect.png)

* JSON con IPs

---

### 🔹 Resolución DNS interna

El cliente puede acceder a la API mediante el nombre:

api

Esto demuestra:

* Docker implementa DNS interno
* No es necesario usar IPs

---

## 🧠 Análisis técnico

* Docker crea una red bridge automáticamente
* Cada servicio recibe una IP privada
* Los servicios se comunican por nombre (DNS interno)
* No se utiliza localhost

---

## 📌 Conceptos aplicados

* Redes internas (bridge)
* DNS en contenedores
* Cliente-servidor distribuido
* Comunicación entre servicios

---

## 📌 Conclusiones

* Se logró comunicación entre contenedores sin usar IPs manuales
* Se validó el uso de DNS interno de Docker
* Se comprendió cómo se estructuran sistemas distribuidos básicos

---

## 🚀 Próximos pasos

* Simular múltiples APIs
* Introducir balanceo de carga
* Aplicar subnetting a redes simuladas
