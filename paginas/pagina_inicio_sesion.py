"""Page Object de la página de inicio de sesion de SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as condiciones
from selenium.webdriver.support.ui import WebDriverWait

from configuracion.config import ESPERA_EXPLICITA_SEGUNDOS


class PaginaInicioSesion:
    """Localizadores en la página de inicio de sesión."""

    CAMPO_USUARIO = (By.ID, 'user-name')
    CAMPO_CONTRASENA = (By.ID, 'password')
    BOTON_INICIAR_SESION = (By.ID, 'login-button')
    MENSAJE_ERROR = (By.CSS_SELECTOR, '[data-test="error"]')


    """Localizador del contenedor de inventario tras un inicio de sesión exitoso."""
    CONTENEDOR_INVENTARIO = (By.ID, 'inventory_container')


    """"Acciones en la página de inicio de sesión."""

    def __init__(self, navegador: WebDriver) -> None:
        self.navegador = navegador
        self.espera = WebDriverWait(navegador, ESPERA_EXPLICITA_SEGUNDOS)


    """Rellena los campos de las credenciales y envia el formulario."""
    def iniciar_sesion(self, usuario: str, contrasena: str) -> None:
        campo_usuario = self.espera.until(condiciones.visibility_of_element_located(self.CAMPO_USUARIO))
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

        campo_contrasena = self.espera.until(condiciones.visibility_of_element_located(self.CAMPO_CONTRASENA))
        campo_contrasena.clear()
        campo_contrasena.send_keys(contrasena)

        boton_iniciar_sesion = self.espera.until(condiciones.element_to_be_clickable(self.BOTON_INICIAR_SESION))
        boton_iniciar_sesion.click()


    """Espera a que el inventario sea visible tras un acceso exitoso."""
    def esperar_inventario(self) -> WebElement:
        """Espera a que el inventario sea visible tras un acceso exitoso."""
        return self.espera.until(condiciones.visibility_of_element_located(self.CONTENEDOR_INVENTARIO))


    """Obtiene el mensaje de error tras un acceso fallido."""
    def obtener_mensaje_error(self) -> str:
        mensaje = self.espera.until(condiciones.visibility_of_element_located(self.MENSAJE_ERROR))
        return mensaje.text
