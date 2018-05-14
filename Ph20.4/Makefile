#Generate completed assignment PDF
.PHONY : pdf
pdf : set4.tex *.png vc.log
	pdflatex $<

#Generate version control log
vc.log :
	git log > $@

# Generate plots
%.png : ode.py
	python $< 0 0.8 100000 0.001 # Change python code command line arguments


.PHONY : clean
clean :
	rm -f *.png
	rm set4.pdf
	rm set4.aux
	rm set4.log
	rm set4.out
	rm vc.log
