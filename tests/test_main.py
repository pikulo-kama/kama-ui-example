

class TestMain:

    def test_main(self, module_patch):

        from kexample.main import main

        app_mock = module_patch("KamaApplication")
        sys_exit_mock = module_patch("sys.exit")

        main()

        app_mock.assert_called_once()
        app_mock().exec.assert_called_once()

        sys_exit_mock.assert_called_once_with(app_mock().exec.return_value)
