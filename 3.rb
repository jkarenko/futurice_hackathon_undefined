# 3. Pair Isograms
# Pair isogram means a word which has two of each letter which are in the
# word. For example, word poop is a pair isogram because each of its letter is
# twice in the word. For example bee is not a pair isogram because b is there
# only once.
# Problem
# When given a list of words, find out which are pair isograms.
# Input
# List of words separated by space.
# Output
# Print only the pair isograms, separated by space.
# Sample Input
# poop bee
# Sample Output
# poop


def print_pair_isograms(words)
  pair_isograms = []
  words.each do |word|
    chars = {}
    word.each_char do |c|
      if chars.has_key? c
        chars[c] += 1
      else
        chars[c] = 1
      end
    end
    if chars.select{|k, v| v != 2}.size == 0
      pair_isograms.push word
    end
  end
  puts pair_isograms
end


print_pair_isograms(["poop", "bee", "lololo", "abebapoeop"])
