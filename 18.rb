# file_names = ["words.txt"]
file_names = ["english.100MB", "proteins.100MB"]

file_names.each do |filename|
  freq = {}
  File.foreach(filename) do |x|
    for i in 0..x.size - 3
      s = x[i..i + 2]
      if freq.has_key? s
        freq[s] += 1
      else
        freq[s] = 1
      end
    end
  end

  most_frequent = freq.select {|k, v| v == freq.values.max }.keys.first.to_s
  cmd = "awk '{gsub(\"" + most_frequent + "\",\"£\");print}' #{filename} > #{filename}.compressed"
  system(cmd)
  puts "#{filename}: #{File.size(filename)} -> #{filename + ".compressed"}: #{File.size(filename + ".compressed")}"
end

puts "code file size: #{File.size('18.rb')}"
