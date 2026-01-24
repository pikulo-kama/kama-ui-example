from kui.component.button import KamaPushButton
from kui.core.controller import WidgetController
from kui.core.metadata import ControllerArgs
from kui.core.shortcut import add_dynamic_data, dynamic_data


class IncrementButtonController(WidgetController):

    def setup(self, button: KamaPushButton, args: ControllerArgs):

        def on_click():
            counter_value = dynamic_data("counter") or 0
            add_dynamic_data("counter", counter_value + 1)

            self.manager.event_refresh("counter_value_change")

        button.clicked.connect(on_click)


class DecrementButtonController(WidgetController):

    def setup(self, button: KamaPushButton, args: ControllerArgs):
        def on_click():
            counter_value = dynamic_data("counter") or 0
            add_dynamic_data("counter", max(counter_value - 1, 0))

            self.manager.event_refresh("counter_value_change")

        button.clicked.connect(on_click)


class ResetButtonController(WidgetController):

    def setup(self, button: KamaPushButton, args: ControllerArgs):
        def on_click():
            add_dynamic_data("counter", 0)
            self.manager.event_refresh("counter_value_change")

        button.clicked.connect(on_click)
