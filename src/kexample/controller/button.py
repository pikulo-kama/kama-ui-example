from kui.component.button import KamaPushButton
from kui.core.controller import WidgetController
from kui.core.metadata import ControllerArgs
from kui.core.shortcut import add_dynamic_data, dynamic_data, tr


class IncrementButtonController(WidgetController):

    def setup(self, button: KamaPushButton, args: ControllerArgs):

        def on_click():
            counter_value = (dynamic_data("counter") or 0) + 1
            pseudo_mode_active = dynamic_data("isPseudoModeActivated")
            add_dynamic_data("counter", counter_value)

            if counter_value == 11 and not pseudo_mode_active:
                add_dynamic_data("isPseudoModeActivated", True)
                self.application.translations.locale = "en_PSEUDO"
                self.manager.refresh()

                self.application.window.notification(tr("message_PseudoModeOn"))

            else:
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
            pseudo_mode_active = dynamic_data("isPseudoModeActivated")

            if pseudo_mode_active:
                self.application.translations.locale = None
                add_dynamic_data("isPseudoModeActivated", False)
                self.manager.refresh()

                self.application.window.notification(tr("message_PseudoModeOff"))

            else:
                self.manager.event_refresh("counter_value_change")

        button.clicked.connect(on_click)
