# ProjectEuler.net
# Problem8
# William Martin
# 2/22/2018

n = "73167176531330624919225119674426574742355349194934969835203127" \
    "74506326239578318016984801869478851843858615607891129494954595" \
    "01737958331952853208805511125406987471585238630507156932909632" \
    "95227443043557668966489504452445231617318564030987111217223831" \
    "13622298934233803081353362766142828064444866452387493035890729" \
    "62904915604407723907138105158593079608667017242712188399879790" \
    "87922749219016997208880937766572733300105336788122023542180975" \
    "12545405947522435258490771167055601360483958644670632441572215" \
    "53975369781797784617406495514929086256932197846862248283972241" \
    "37565705605749026140797296865241453510047482166370484403199890" \
    "00889524345065854122758866688116427171479924442928230863465674" \
    "81391912316282458617866458359124566529476545682848912883142607" \
    "69004224219022671055626321111109370544217506941658960408071984" \
    "03850962455444362981230987879927244284909188845801561660979191" \
    "33875499200524063689912560717606058861164671094050775410022569" \
    "83155200055935729725716362695618826704282524836008232575304207" \
    "52963450"
import time




# returns True if parameter n contains a zero
# Not used for this problem as 'if "0" not in curr_slice:' is more efficient
def has_zero(n):
    for d in n:
        if int(d) == 0:
            return True

# returns product of numbers in a list
def multiply(num_list):
    total = 1
    for x in num_list:
        total *= x
    return total


# check slice of parameter n for # of characters specificed
def slice(n, chars = 1):
    max = 0
    for i,v in enumerate(n):
        curr_slice = (n[i:i+chars])
        # skip any slice containing a zero since product would be zero
        if "0" not in curr_slice:
        # if not has_zero(curr_slice):
            # ensure current slice has the number of digits needed
            if len(curr_slice) == chars:
                # creates variable for product of current slice
                curr_product = multiply(list(int(x) for x in curr_slice))
                if curr_product > max:
                    max = curr_product
    return max

start = time.time()
ans = (slice(n,13))
elapsed = (time.time()- start)

print("Found %s in %s seconds" %(ans, elapsed))

# Found 23514624000 in 0.0009999275207519531 seconds without has_zero function
# Found 23514624000 in 0.003000020980834961 seconds with has_zero function
