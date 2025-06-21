# 🎯 OSM Bot - Online Soccer Manager Automation

Bot automatizado para ver anuncios en [Online Soccer Manager](https://en.onlinesoccermanager.com/) de forma infinita usando Selenium y Python.

## ✨ Características

- 🔐 **Login automático** con tus credenciales
- 🛒 **Navegación automática** al modal de store
- 📺 **Loop infinito de anuncios** - Ve anuncios automáticamente
- ⏰ **Manejo inteligente de límites** - Detecta timeouts y espera el tiempo correcto
- 🔄 **Autorecuperación** - Se reinicia automáticamente si algo falla
- 🔇 **Chrome silencioso** - Inicia muteado para no molestar
- 📊 **Contador de anuncios** - Lleva estadísticas de anuncios vistos
- 🛡️ **Resistente a errores** - Maneja timeouts y problemas de conexión

## 🚀 Instalación Rápida

### 1. Instalar Python
Asegúrate de tener **Python 3.7+** o superior:
```bash
python --version
```

### 2. Instalar Selenium
```bash
pip install selenium
```

O usando el archivo de dependencias:
```bash
pip install -r requirements.txt
```

### 3. Instalar Google Chrome
El bot requiere **Google Chrome** instalado en tu sistema.

## ⚙️ Configuración

### 📝 Editar Credenciales
Abre `osm_ad_bot.py` y cambia estas líneas con tus credenciales reales:

```python
# Líneas 18-19
USERNAME = "tu_usuario_real"      # ← Cambiar aquí
PASSWORD = "tu_contraseña_real"   # ← Cambiar aquí
```

## 🎮 Uso

### Ejecutar el Bot
```bash
cd osm-clicker
python osm_ad_bot.py
```

### Primera Ejecución
Si no configuraste credenciales, el bot te preguntará si quieres hacer pruebas.

## 📋 Secuencia Automática

El bot ejecuta estos pasos automáticamente:

1. 🌐 **Navega** a Online Soccer Manager
2. ⏳ **Espera** a que cargue la página
3. ✅ **Acepta** términos y condiciones ("Accept")
4. 🔑 **Clickea** "Log in"
5. 👤 **Ingresa** nombre de usuario
6. 🔒 **Ingresa** contraseña  
7. 🚪 **Clickea** botón de login
8. 💰 **Clickea** div "balances"
9. 🛒 **Espera** modal store y hace scroll horizontal
10. 📺 **Loop infinito**: Busca y clickea "Watch ad" continuamente

## 🤖 Automatización Inteligente

### 📺 Loop de Anuncios
- Busca botones "Watch ad"
- Clickea automáticamente
- Espera hasta 5 minutos (300 segundos) por anuncio
- Continúa al siguiente anuncio
- **Cuenta total** de anuncios vistos

### ⏰ Manejo de Límites
Cuando aparece el mensaje de límite, el bot:

| Mensaje Detectado | Acción |
|-------------------|--------|
| "an hour" | Espera 61 minutos + intentos cada 3 min |
| "a few seconds" | Espera 1 minuto + intentos cada 3 min |
| "X minutes" | Espera X+1 minutos + intentos cada 3 min |
| Mensaje genérico | Intentos cada 3 minutos directamente |

### 🔄 Autorecuperación
El bot detecta y maneja automáticamente:
- ❌ **Timeouts de botones** → Reinicia desde paso 8
- ❌ **Modal no carga** → Refresh + reinicio
- ❌ **Anuncios colgados** → Reinicia automáticamente
- ❌ **Conexión perdida** → Espera y reintenta

## 🛑 Control del Bot

### Detener el Bot
- **Ctrl+C**: Detiene el loop y muestra estadísticas
- **Enter**: Cierra el navegador (después de Ctrl+C)

### Información en Tiempo Real
```
📺 Anuncio #15 - Clickeando 'Watch ad'...
⏳ Esperando a que termine el anuncio...
✅ Anuncio #15 completado. Preparando siguiente anuncio...
🔍 Buscando botón 'Watch ad' (Anuncio #16)...
```

## 🔧 Configuración Avanzada

### Chrome Options Configuradas
```python
chrome_options.add_argument("--start-maximized")     # Ventana maximizada
chrome_options.add_argument("--disable-notifications") # Sin notificaciones
chrome_options.add_argument("--mute-audio")           # Sin sonido
```

### Timeouts Configurados
- **Límites**: 3 segundos para detectar mensajes
- **Botones**: 10 segundos para encontrar elementos
- **Anuncios**: 300 segundos (5 minutos) para completar
- **Reintentos**: Cada 3 minutos cuando hay límites

## 🐛 Solución de Problemas

### Chrome no se abre
```bash
# Verificar instalación de Chrome
google-chrome --version   # Linux
# O buscar Chrome en aplicaciones
```

### Error de credenciales
- Verificar usuario y contraseña en tu cuenta OSM
- Asegurar que no hay caracteres especiales problemáticos

### Bot se queda "colgado"
- El bot tiene autorecuperación - espera unos minutos
- Si persiste, usar Ctrl+C y reiniciar

### Anuncios no aparecen
- Verificar que estás en la sección correcta del juego
- El bot maneja automáticamente límites de anuncios

## 📊 Estadísticas

Al finalizar el bot muestra:
```
🛑 Loop de anuncios detenido por el usuario
📊 Total de anuncios vistos: 47
```

## ⚠️ Consideraciones Importantes

### Términos de Servicio
- **Úsalo responsablemente** - Respeta los términos de OSM
- **No abuses** - No ejecutes múltiples instancias simultáneas
- **Uso personal** - Solo para tu propia cuenta

### Seguridad
- **No compartas** el archivo con tus credenciales
- **Mantén privadas** tus credenciales
- **Úsalo en redes confiables**

### Rendimiento
- **Una instancia por cuenta** - No ejecutes múltiples bots
- **Conexión estable** - Mejor en WiFi estable
- **Recursos del sistema** - Chrome consume memoria

## 📁 Estructura del Proyecto

```
osm-clicker/
├── osm_ad_bot.py          # Script principal del bot
├── requirements.txt    # Dependencias de Python
└── README.md          # Este archivo
```

## 🚀 Ejecución en Background

### Windows
```bash
# Ejecutar en background
start /b python osm_ad_bot.py
```

### Linux/macOS
```bash
# Ejecutar en background
nohup python osm_ad_bot.py &
```

## 🆕 Actualizaciones

Para obtener nuevas características:
1. Descargar la versión actualizada
2. Mantener tus credenciales configuradas
3. Verificar cambios en requirements.txt

## 📞 Soporte

Si encuentras problemas:
1. Verificar que Chrome esté actualizado
2. Verificar conexión a internet
3. Revisar credenciales
4. Reiniciar el bot

---

**¡A conseguir fichitas! 🎮⚽**
