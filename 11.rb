boxes = [[2,2,9], [6,5,5], [1,4,9], [3,1,1]]
permutations = []

def find_largest_base(permutations)
  largest = permutations[0]
  permutations.each do |perm|
    largest = perm if get_box_base_area(perm) > get_box_base_area(largest)
  end
  return largest
end

def find_smallest_base(permutations)
end

def get_box_base_area(box)
  return box[0] * box[1]
end

boxes.each do |box|
  permutations.push box.permutation(2).to_a.uniq
end

permutations.each do |box|
  # print box.to_s + "\n"
  box.each do |perm|

  end
end

print find_largest_base(permutations[2])



# [2, 2][2, 9][9, 2]
# [6, 5][5, 6][5, 5]
# [1, 4][1, 9][4, 1][4, 9][9, 1][9, 4]
# [3, 1][1, 3][1, 1]
