
hvc:
	@$(shell sleep 1.13)
	@cp src/hvc.py hvc
	@chmod +x hvc

clean:
	rm hvc