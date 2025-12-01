import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Conectamos con tu conftest.py
@pytest.mark.usefixtures("driver_setup")
class TestRecorder:

    # ---------------------------------------------------------
    # HELPER: Función WAIT
    # ---------------------------------------------------------
    def wait_for_element(self, by, value, timeout=100):
        """
        Helper para esperar explícitamente a un elemento.
        Usa self.driver que viene inyectado desde el conftest.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def test_run_recorder(self):

        driver = self.driver

        print("\n--- Iniciando Ejecución de Pasos Grabados ---")


        # ---------------------------------------------------------
        # ESPACIO PARA PEGAR CÓDIGO (APPIUM RECORDER)
        # ---------------------------------------------------------

        # Pega aquí directamente lo que te dio el Inspector.
        # No necesitas indentar nada especial ni poner try/except.
        # Asegúrate de sí usar la función self.wait_for_element(...) cuando sea requerida
        # el1 = self.wait_for_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        # el1.click()
        """ingreso"""
        el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Usuario")
        el2.click()
        el2.send_keys("anevvv001")
        el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Contraseña")
        el3.click()
        el3.send_keys("Pwst12345*")
        el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Servidor")
        el4.click()
        el4.clear()
        el4.send_keys("dsr-mobile.pwstasp.com.uy/mobileservices")
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.CheckBox")
        el5.click()
        el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Instalar\")")
        el6.click()
        """carga"""
        el7 = self.wait_for_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"cargar\")")
        el7.click()
        """"aceptar permisos"""
        el8 = self.wait_for_element(by=AppiumBy.ID, value="com.android.packageinstaller:id/permission_allow_button")
        el8.click()
        el9 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
        el9.click()



        # ---------------------------------------------------------
        # FIN DEL CÓDIGO PEGADO
        # ---------------------------------------------------------

        # Pequeña pausa final opcional para que veas el resultado antes de que se cierre
        time.sleep(2)
        print("--- Fin de los pasos grabados ---")

