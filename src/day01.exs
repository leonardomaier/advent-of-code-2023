file_path = Path.expand("./inputs/day01.txt")

case File.read(file_path) do
  {:ok, content} ->
    result = content
    |> String.split("\n")
    |> Enum.map(&String.replace(&1, ~r/[^0-9]/, ""))
    |> Enum.map(&String.at(&1, 0) <> String.at(&1, -1) |> String.to_integer)
    |> Enum.sum

    IO.inspect(result)
  {:error, reason} -> IO.puts("#{reason}")
end
