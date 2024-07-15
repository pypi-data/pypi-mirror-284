import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
  _component_func = components.declare_component(
    "chat_message",
    url="http://localhost:3001",
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/build")
  _component_func = components.declare_component("chat_message", path=build_dir)


def chat_message(msg, user, appendUser, appendTime, key=None):
    """Create a new instance of "chat_message".

    Parameters
    ----------
    msg
      - Message object including author
    user
      - Current user (from session state)
    appendUser
      - Append the user's name and profile image to message?
    appendTime
      - Append the message time?
    key
      - NEEDS TO REMAIN None FOR SOME REASON!

    Returns
    -------
    Message
      - Returns message object when clicked.
        
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(message=msg, user=user, appendUser=appendUser, appendTime=appendTime, key=key, default=False)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value






