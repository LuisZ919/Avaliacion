# Avaliación  
**Exercicio:** Desenvolvemento e integración de scripts en Python  
**Autor:** Luis García  

---

## Descrición do proxecto

Este proxecto ten como obxectivo integrar dous scripts en Python que interactúan cunha API, unha base de datos MongoDB e ferramentas de manexo de datos para extraer, almacenar e exportar información. O exercicio tamén inclúe opcións avanzadas para despregar a aplicación en contornas containerizadas e na nube.

A API empregada é [CityBikes](https://citybik.es/), que ofrece información en tempo real sobre estacións de aparcamento de bicicletas en servizos de aluguer de todo o mundo.

---

## Estrutura do proxecto

### **Parte básica (obrigatoria)**

1. **Script 1:**  
   - Conéctase á API de CityBikes a intervalos regulares.
   - Obtén os datos e almacénaos nunha base de datos MongoDB.
   - O script corre de forma indefinida ata que se detén manualmente.

2. **Script 2:**  
   - Le os datos almacenados en MongoDB e cárgaos nun `DataFrame` de pandas.
   - Exporta os datos seleccionados aos formatos **CSV** e **Parquet**.

---

### **Parte avanzada (opcional)**

1. **Dockerización:**
   - Creouse unha imaxe Docker para a aplicación. Esta imaxe está publicada en Docker Hub:
     - [Docker Hub: luisz919/citybikes_app:latest](https://hub.docker.com/r/luisz919/citybikes_app)
   - Utilízanse contedores Docker para a aplicación e para un servidor MongoDB.
   
2. **Despregue na nube (OpenStack):**
   - A aplicación está implementada nunha instancia OpenStack con MongoDB e os scripts configurados.
   - A execución mantense activa durante as vacacións, almacenando aproximadamente **2016 documentos** no período.

3. **Automatización:**
   - Os scripts están configurados como servizos do sistema para executar de forma autónoma.
   - A base de datos almacena información persistente con opción de exportación.

---

## Instrucións de uso

### **1. Clonar o repositorio**
```bash
git clone https://github.com/luisz919/citybikes-app.git
cd citybikes-app
