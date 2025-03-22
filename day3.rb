def is_number_good(str_number)
	good_number = /^\-?[0-9]+$/
	if str_number.match(good_number)
		#puts "good number -> " + str_number
		return true
	else
		#puts "bad number -> " + str_number
		return false
	end
end

def pars_mul_internals(str_mul_internals)
	match_is_ok = true
	str_mul_internals.split(",").each do |number|
		res_number = is_number_good(number)
		if res_number == false
			match_is_ok = false
			break
		end
	end
	if match_is_ok == false
		#puts "'"+str_mul_internals+"' -> not ok"
		return 0
	else
		multiplied = 1
		str_mul_internals.split(",").map { |x| multiplied *= x.to_i }
		#puts "'"+str_mul_internals+"' -> "+multiplied.to_s
		return multiplied
	end
end

def day3(str_memory)
	sum = 0
	str_memory.scan(/mul\(([0-9\-,]+)\)/).each do |matches|
		sum += pars_mul_internals(matches[0])	
	end
	return sum
end

def unittest_day()
	raise "oops" unless (is_number_good("") == false)
	raise "oops" unless (is_number_good("_") == false)
	raise "oops" unless (is_number_good(" ") == false)
	raise "oops" unless (is_number_good("5") == true)
	raise "oops" unless (is_number_good("-5") == true)
	raise "oops" unless (is_number_good("--5") == false)
	raise "oops" unless (is_number_good("+5") == false)
	#	
	raise "oops" unless (day3("mul(2,-,,3,4,5)") == 0)
	str_day3 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
	raise "oops" unless (day3(str_day3) == 161)
	raise "oops" unless (day3("mul(2,3,4,5)") == 120)
	raise "oops" unless (day3("mul(2,3,4,5)cosijroweir231:'[.,244mul(45,45jwoivfmul(2,3,-4)(") == 120+(-24))
end

unittest_day()

str_day3 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
puts "2025 Day3 string -> "+str_day3
puts "result -> "+day3(str_day3).to_s
