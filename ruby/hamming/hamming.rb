class Hamming
  def self.compute(strand_a, strand_b)
    raise ArgumentError, "The strands must have the same length" unless strand_a.length == strand_b.length
    return strand_a.split("").zip(strand_b.split("")).count { |a, b| a != b}
  end
end
