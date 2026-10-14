"""Pruebas funcionales del inicio de sesion de SauceDemo."""

from datos.usuarios_prueba import (
    CONTRASENA,
    USUARIO_ERROR,
    USUARIO_BLOQUEADO,
    USUARIO_ESTANDAR,
    USUARIO_PROBLEMA,
    USUARIO_RENDIMIENTO_LENTO,
    USUARIO_VISUAL,
)
from paginas.pagina_inicio_sesion import PaginaInicioSesion


class TestInicioSesion:
    """Casos de prueba para cada usuario listado en el portal de inicio de sesion."""


    """Verifica el acceso del usuario estandar."""
    def test_inicio_sesion_usuario_estandar(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_ESTANDAR, CONTRASENA)
        assert pagina_inicio_sesion.esperar_inventario().is_displayed()


    """Verifica el acceso de problem_user."""
    def test_inicio_sesion_usuario_problema(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_PROBLEMA, CONTRASENA)
        assert pagina_inicio_sesion.esperar_inventario().is_displayed()


    """Verifica el acceso de performance_glitch_user."""
    def test_inicio_sesion_usuario_retraso(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_RENDIMIENTO_LENTO, CONTRASENA)
        assert pagina_inicio_sesion.esperar_inventario().is_displayed()


    """Verifica el acceso de error_user."""
    def test_inicio_sesion_usuario_error(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_ERROR, CONTRASENA)
        assert pagina_inicio_sesion.esperar_inventario().is_displayed()


    """Verifica el acceso de visual_user."""
    def test_inicio_sesion_usuario_visual(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_VISUAL, CONTRASENA)
        assert pagina_inicio_sesion.esperar_inventario().is_displayed()


    """Verifica que locked_out_user no pueda acceder."""
    def test_inicio_sesion_usuario_bloqueado(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_BLOQUEADO, CONTRASENA)
        assert (pagina_inicio_sesion.obtener_mensaje_error()== "Epic sadface: Sorry, this user has been locked out.")


    """Verifica el mensaje al enviar credenciales incorrectas."""
    def test_inicio_sesion_credenciales_incorrectas(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion("usuario_inexistente", "contrasena_incorrecta")
        assert (pagina_inicio_sesion.obtener_mensaje_error()== "Epic sadface: Username and password do not match any user in this service")


    """Verifica la validacion del usuario obligatorio."""
    def test_inicio_sesion_usuario_vacio(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion("", CONTRASENA)
        assert pagina_inicio_sesion.obtener_mensaje_error() == "Epic sadface: Username is required"


    """Verifica la validacion de la contrasena obligatoria."""
    def test_inicio_sesion_contrasena_vacia(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion(USUARIO_ESTANDAR, "")
        assert pagina_inicio_sesion.obtener_mensaje_error() == "Epic sadface: Password is required"


    """Verifica la validacion cuando ambos campos estan vacios."""
    def test_inicio_sesion_credenciales_vacias(self, pagina_inicio_sesion: PaginaInicioSesion) -> None:
        pagina_inicio_sesion.iniciar_sesion("", "")
        assert pagina_inicio_sesion.obtener_mensaje_error() == "Epic sadface: Username is required"
