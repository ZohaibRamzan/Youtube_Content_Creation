import streamlit as st
def main():
    st.title("Session Example")

    # Incrementing counter
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    if st.button("Increment Counter"):
        st.session_state.counter += 1

    st.write(f"Counter Value: {st.session_state.counter}")

    st.write(st.session_state)


if __name__ == "__main__":
    main()
