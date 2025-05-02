from main import main


def test_main():
    # Simple test to check if the main function runs without errors
    try:
        main()
    except Exception as e:
        assert False, f"main() raised an exception: {e}"
