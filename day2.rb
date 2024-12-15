
class Report
	def initialize(v1,v2,v3,v4,v5)
		@@v = [v1,v2,v3,v4,v5]
	end

	def to_s()
		@@v.join(",")
	end

	def test()
		lv = @@v
		diffs = [lv[1] - lv[0], lv[2] - lv[1], lv[3] - lv[2], lv[4] - lv[3]]
		diffs.each do |v|
			# all values must differ (no diff == 0 allowed)
			if v == 0
				return false
			else
				# the change not greater than 3
				if v.abs() > 3
					return false
				else
					# all changes must have the same sign (+ or -)
					if ((v <=> 0) != (diffs[0] <=> 0))
						return false
					end
				end
			end
		end
		# passed everything - good one
		return true
	end
end

raise "oops" unless Report.new(1,2,3,4,5).test() == true

raise "oops" unless Report.new(7,6,4,2,1).test() == true
raise "oops" unless Report.new(1,2,7,8,9).test() == false
raise "oops" unless Report.new(9,7,6,2,1).test() == false
raise "oops" unless Report.new(1,3,2,4,5).test() == false
raise "oops" unless Report.new(8,6,4,4,1).test() == false
raise "oops" unless Report.new(1,3,6,7,9).test() == true

class ReportList
	@@reps

	def fromLines(lines)
		#puts "got param -> '#{lines}'"
		cnt = 0 # count good reports
		lines.each do |line|
			m = line.match(/\s*(\-*[0-9]+)\s+(\-*[0-9]+)\s+(\-*[0-9]+)\s+(\-*[0-9]+)\s+(\-*[0-9]+)\s*/)
			if m
				#puts "yes"
				#puts m
				nums = m[1..5].map(&:to_i)
				#puts "converted nums -> #{nums}"
				r = Report.new(nums[0],nums[1],nums[2],nums[3],nums[4])
				if r.test()
					cnt += 1
				end
			end
		end
		return cnt
	end
end


rl = ReportList.new
raise "oops" unless rl.fromLines(["1 2 3 4 6","3 3 4 5 3"]) == 1

const_day2_example = %{
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
}.split("\n")

raise "oops" unless rl.fromLines(const_day2_example) == 2

# the data needed ....
const_day2_part2 = %{
}.split("\n")

puts "part2 answer is -> #{rl.fromLines(const_day2_part2)}"
