from scipy import signal

def butterWorthFilter(Input,w,order,typeFilter):
	b,a = signal.butter(order, w, typeFilter)
	output = signal.filtfilt(b, a, Input,padlen=0)
	return output

