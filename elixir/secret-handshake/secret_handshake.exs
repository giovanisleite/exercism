defmodule SecretHandshake do
  @doc """
  Determine the actions of a secret handshake based on the binary
  representation of the given `code`.

  If the following bits are set, include the corresponding action in your list
  of commands, in order from lowest to highest.

  1 = wink
  10 = double blink
  100 = close your eyes
  1000 = jump

  10000 = Reverse the order of the operations in the secret handshake
  """
  @spec commands(code :: integer) :: list(String.t())
  def commands(code) do
    use Bitwise
    codes = %{"wink" => 1, "double blink" => 2, "close your eyes" => 4, "jump" => 8}
    maybe_reverse = fn(list, bool) -> (if bool, do: Enum.reverse(list), else: list) end
    ["wink", "double blink", "close your eyes", "jump"]
    |> Enum.filter(fn(action) -> band(code, codes[action]) > 0 end)
    |> maybe_reverse.(band(code, 16) > 0)
  end
end
