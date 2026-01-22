import sys
from kui.core.app import KamaApplication


def main():
    sys.exit(KamaApplication().exec())


if __name__ == "__main__":  # pragma: no cover
    main()
