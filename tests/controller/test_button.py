import pytest
from pytest_mock import MockerFixture


class TestIncrementButtonController:

    def test_increment(self, mocker: MockerFixture, module_patch):
        """
        Tests that the increment controller adds 1 to the current count.
        """

        from kexample.controller.button import IncrementButtonController
        from kui.core.metadata import ControllerArgs

        button = mocker.MagicMock()
        application = mocker.MagicMock()
        manager = mocker.MagicMock()
        controller = IncrementButtonController(application, manager)

        module_patch("dynamic_data", return_value=5)
        add_dynamic_data_mock = module_patch("add_dynamic_data")

        controller.setup(button, ControllerArgs({}))

        on_click_callback = button.clicked.connect.call_args[0][0]
        on_click_callback()

        add_dynamic_data_mock.assert_called_once_with("counter", 6)
        manager.event_refresh.assert_called_once_with("counter_value_change")


class TestDecrementButtonController:

    @pytest.mark.parametrize("initial_value, result_value", [
        (0, 0),
        (6, 5)
    ])
    def test_decrement(self, mocker: MockerFixture, module_patch, initial_value, result_value):
        """
        Tests that the decrement controller respects the max(0) constraint.
        """

        from kexample.controller.button import DecrementButtonController
        from kui.core.metadata import ControllerArgs

        button = mocker.MagicMock()
        application = mocker.MagicMock()
        manager = mocker.MagicMock()
        controller = DecrementButtonController(application, manager)

        module_patch("dynamic_data", return_value=initial_value)
        add_dynamic_data_mock = module_patch("add_dynamic_data")

        controller.setup(button, ControllerArgs({}))

        on_click_callback = button.clicked.connect.call_args[0][0]
        on_click_callback()

        add_dynamic_data_mock.assert_called_once_with("counter", result_value)
        manager.event_refresh.assert_called_once_with("counter_value_change")


class TestResetButtonController:

    def test_reset(self, mocker: MockerFixture, module_patch):
        """
        Tests that the reset controller always sets the counter to 0.
        """

        from kexample.controller.button import ResetButtonController
        from kui.core.metadata import ControllerArgs

        button = mocker.MagicMock()
        application = mocker.MagicMock()
        manager = mocker.MagicMock()

        controller = ResetButtonController(application, manager)

        module_patch("dynamic_data", return_value=100)
        add_dynamic_data_mock = module_patch("add_dynamic_data")

        controller.setup(button, ControllerArgs({}))

        on_click_callback = button.clicked.connect.call_args[0][0]
        on_click_callback()

        add_dynamic_data_mock.assert_called_once_with("counter", 0)
        manager.event_refresh.assert_called_once_with("counter_value_change")
