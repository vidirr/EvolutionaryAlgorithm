__author__ = 'GSUS'


"""double f1(const vector<double>& xs)
    {
        double sum = 0.0;
        for(unsigned int i=0; i<xs.size(); ++i) {
            sum += xs[i] * xs[i];
        }
        return sum;
    } """
def f1(xs):
    sum = 0.0
    for x in xs:
        sum += x**2
    return sum

"""
 double f2(const vector<double>& xs)
 {
    double term1 = (xs[0] * xs[0]) - xs[1];
    double term2 = 1.0 - xs[0];
    return 100 * term1 * term1 + term2 * term2;
 }"""
def f2(xs):
    term1 = xs[0]**2 - xs[1]
    term2 = 1.0 - xs[0]
    return float(100 * term1 * term2 + term2 * term2)

"""
     double f2(const vector<double>& xs)
     {
        static double f5_arr[2][25] = {
            { -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0 },
         { -32.0, -32.0, -32.0, -32.0, -32.0,
           -16.0, -16.0, -16.0, -16.0, -16.0,
           0.0, 0.0, 0.0, 0.0, 0.0,
           16.0, 16.0, 16.0, 16.0, 16.0,
           32.0, 32.0, 32.0, 32.0, 32.0 }
         };

         double x = xs[0];
         double y = xs[1];

         double sum = 0.0;
         for(int i=0; i<=24; ++i) {
            double diff1 = x - f5_arr[0][i];
            double diff2 = y - f5_arr[1][i];
            double subsum=(diff1 * diff1 * diff1 * diff1 * diff1 * diff1) +
            (diff2 * diff2 * diff2 * diff2 * diff2 * diff2);
            subsum += double(i + 1);
            subsum = double(1) / subsum;
            sum += subsum;
         }
        return 500.0 - (1.0 / (0.002 + sum) );
}"""
def shekel(xs):
    f5_arr = [[-32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0]
             [-32.0, -32.0, -32.0, -32.0, -32.0,
              -16.0, -16.0, -16.0, -16.0, -16.0,
              0.0, 0.0, 0.0, 0.0, 0.0,
              16.0, 16.0, 16.0, 16.0, 16.0,
              32.0, 32.0, 32.0, 32.0, 32.0]]
    x = xs[0]
    y = xs[1]
    sum = 0.0

    for i in range(0,25):
        diff1 = x - f5_arr[0][i]
        diff2 = y - f5_arr[1][i]
        subsum = diff1**6 + diff2**6
        subsum += i+1.0
        subsum = 1.0/subsum
        sum += subsum

    return 500.0 - (1.0 / (0.002 + sum))

