"""Fixtures compartidas por la suite de pruebas."""

from collections.abc import Iterator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from configuracion.config import ALTO_VENTANA, ANCHO_VENTANA, URL_BASE
from paginas.pagina_inicio_sesion import PaginaInicioSesion


"""Inicia Chrome para una prueba y lo cierra al terminar."""
@pytest.fixture
def navegador() -> Iterator[WebDriver]:
    opciones = webdriver.ChromeOptions()
    opciones.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    controlador = webdriver.Chrome(options=opciones)
    try:
        controlador.set_window_size(ANCHO_VENTANA, ALTO_VENTANA)
        yield controlador
    finally:
        controlador.quit()


"""Abre SauceDemo y entrega su pagina de inicio de sesion."""
@pytest.fixture
def pagina_inicio_sesion(navegador: WebDriver) -> PaginaInicioSesion:
    pagina = PaginaInicioSesion(navegador)
    navegador.get(URL_BASE)
    return pagina
