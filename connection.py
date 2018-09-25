"""
LangSec - AMQP (Advance Messaging Queue Protocol) Parser
Author(s): Syed Tanveer
Last modified: 09/24/2018

                            --------------------------
                            -- The Connection class --
                            --------------------------

    The connection class is designed to be long-lasting, and carry multiple channels.

                        The connection life-cycle is this:

    - The client opens a TCP/IP connection to the server and sends a protocol header.
    This is the only data the client sends that is not formatted as a method.

    - The server responds with its protocol version and other properties, including
    a list of the security mechanisms that it supports (the Start method).

    - The client selects a security mechanism (Start-ok).

    - The server starts the authentication process, which uses the SASL
    challenge-response model. It sends the client a challenge (Secure).

    - The Client sends an Authentication response (Secure-ok). For example using
    the "plan" mechanism, the response consist of a login name and password.

    - The server repeats the Challenge (Secure) or moves to negotiation, sending
    a set of parameters such as maximum frame size (Tune).

    - The client accepts or lowers these parameters (Tune-ok).

    - The client formally opens the connection and selects a virtual host (Open).

    - The server confirms that the virtual host is a valid choice (Open-ok).

    - The client now uses the connection as desired.

    - One peer (client or server) ends the connection (Close).

    - The other peer hand-shakes the connection end (Close-Ok).

    - The server and the client close their socket connection.

    there is no hand-shaking for errors on connections that are not fully open.

"""

