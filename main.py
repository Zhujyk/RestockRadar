from checker import is_product_available
from notifier import send_notification
from state import load_previous_state, save_current_state


def run():
    try:
        available_now = is_product_available()
    except Exception as e:
        print(f"Check failed: {e}")
        return

    available_before = load_previous_state()

    if available_now and not available_before:
        send_notification()

    save_current_state(available_now)

    print(
        f"Available now: {available_now} | "
        f"Previously available: {available_before}"
    )


if __name__ == "__main__":
    run()
