#Constants to be used in program



draw = 0
trace = 1
scissor = 2

boy = 0
brushpainting = 1
cat = 2 
dolphin = 3 
elephant = 4 
hat = 5
mountains = 6 
seattle = 7
	
haar = 0
hat = 1 
hermite = 2 
laguerre = 3
scissorinal = 4
pwl = 5
quad = 6 
quads = 7
sin = 8




def main():
	print("Generating survey...")
	cnt = 3 #The number of elements in the survey. Starts with three for the three question blocks.
	HeadList = [ [],[],[], ]

	f = open('newSurvey.qsf', 'w')
	qtypes = ['draw', 'trace', 'scissor']

	# sQuestions, cnt = makeQuestion(cnt, scissor, HeadList, cnt-2, img(mountains,7), img(mountains,7), img(mountains,7))
	# dQuestions, cnt = makeQuestion(cnt, draw, HeadList, 2, img(4,7), img(5,7), img(6,7))
	# tQuestions, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(0,7), img(6,7), img(7,3))

	dQuestions, cnt = drawQuestions(cnt, HeadList)
	tQuestions, cnt = traceQuestions(cnt, HeadList)
	sQuestions, cnt = scissorQuestions(cnt, HeadList)

	print(HeadList)

	h1 = makeHead1()
	h2 = makeHead2(cnt)
	b1 = blockDraw(HeadList)
	b2 = blockTrace(HeadList)
	b3 = blockScissor(HeadList)

	out_string = h1 + b1 + b2 + b3 + h2 + dQuestions + tQuestions + sQuestions
	out_string = end(out_string)
	f.write(out_string)

	print('final count:')
	print(cnt)

def drawQuestions(cnt, HeadList):
	questions = ''
	for pic in range(0,7):
		for left in range(0,8):
			for right in range(0,8):
				if right != left:
					q, cnt = makeQuestion(cnt, draw, HeadList, cnt-2, img(pic,left), img(pic,right), '')
					questions += q
	return questions, cnt

def traceQuestions(cnt, HeadList):
	questions = ''
	for trace1 in range(0,8):
		for trace2 in range(0,8):
			q1, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(brushpainting,trace1), img(mountains,trace1), img(seattle,trace2))
			q2, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(brushpainting,trace1), img(mountains,trace2), img(seattle,trace1))
			q3, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(brushpainting,trace2), img(mountains,trace1), img(seattle,trace1))
			questions += q1 + q2 + q3

			q1, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(cat,trace1), img(dolphin,trace1), img(elephant,trace2))
			q2, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(cat,trace1), img(dolphin,trace2), img(elephant,trace1))
			q3, cnt = makeQuestion(cnt, trace, HeadList, cnt-2, img(cat,trace2), img(dolphin,trace1), img(elephant,trace1))
			questions += q1 + q2 + q3
	return questions, cnt

def scissorQuestions(cnt, HeadList):
	questions = ''
	for pic in range(0,7):
		for left in range(0,8):
			for right in range(0,8):
				if right != left:
					q, cnt = makeQuestion(cnt, scissor, HeadList, cnt-2, img(pic, scissor), img(pic,left), img(pic,right))
					questions += q
	return questions, cnt

def makeHead1():
	h1 = '{"SurveyEntry":{"SurveyID":"SV_6WMJjyJENCW4L6l","SurveyName":"Curve Approximation Aesthetics (template)","SurveyDescription":null,"SurveyOwnerID":"UR_cCu6YyQAc7N5Bf7","SurveyBrandID":"oregonstate","DivisionID":null,"SurveyLanguage":"EN","SurveyActiveResponseSet":"RS_3ydDuuDeA5tnma9","SurveyStatus":"Inactive","SurveyStartDate":"0000-00-00 00:00:00","SurveyExpirationDate":"0000-00-00 00:00:00","SurveyCreationDate":"2015-01-12 17:55:50","CreatorID":"UR_cCu6YyQAc7N5Bf7","LastModified":"2015-01-12 18:00:02","LastAccessed":"0000-00-00 00:00:00","LastActivated":"0000-00-00 00:00:00","Deleted":null},\n\n'
	h1 += '"SurveyElements":[{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"BL","PrimaryAttribute":"Survey Blocks","SecondaryAttribute":null,"TertiaryAttribute":null,"Payload":[\n\n'
	return h1

def blockDraw(HeadList):
	b1 = '{"Type":"Default","Description":"Which given shape would take the longest to draw?","ID":"BL_3EqXIMQGnhMFO0B","BlockElements":['
	for qnum in HeadList[draw]:
		b1 += '{"Type":"Question","QuestionID":"QID' + str(qnum) + '"},'
	b1 = b1[:-1] + ']},\n\n'
	return b1

def blockTrace(HeadList):
	b2 = '{"Type":"Standard","SubType":"","Description":"Which given shape would take the longest to trace?","ID":"BL_8izrvqPrbjFKjwV","BlockElements":['
	for qnum in HeadList[trace]:
		b2 += '{"Type":"Question","QuestionID":"QID' + str(qnum) + '"},'
	b2 = b2[:-1] + ']},\n\n'
	return b2

def blockScissor(HeadList):
	b3 = '{"Type":"Standard","SubType":"","Description":"Which given shape would take the longest to cut out with scissors?","ID":"BL_4PcmQtBqlxchva5","BlockElements":['
	for qnum in HeadList[scissor]:
		b3 += '{"Type":"Question","QuestionID":"QID' + str(qnum) + '"},'
	b3 = b3[:-1] + ']}]},\n\n'
	return b3

def makeHead2(surveycount):
	h2 = '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"FL","PrimaryAttribute":"Survey Flow","SecondaryAttribute":null,"TertiaryAttribute":null,"Payload":{"Flow":[{"ID":"BL_3EqXIMQGnhMFO0B","Type":"Block","FlowID":"FL_2"},{"ID":"BL_8izrvqPrbjFKjwV","Type":"Standard","FlowID":"FL_3"},{"ID":"BL_4PcmQtBqlxchva5","Type":"Standard","FlowID":"FL_4"}],"Properties":{"Count":4},"FlowID":"FL_1","Type":"Root"}},\n\n'
	h2 += '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"SO","PrimaryAttribute":"Survey Options","SecondaryAttribute":null,"TertiaryAttribute":null,"Payload":{"BackButton":"false","SaveAndContinue":"true","SurveyProtection":"PublicSurvey","BallotBoxStuffingPrevention":"false","NoIndex":"Yes","SurveyExpiration":"None","SurveyTermination":"DefaultMessage","Header":"","Footer":"","ProgressBarDisplay":"None","PartialData":"+1 week","ValidationMessage":"","PreviousButton":"  <<  ","NextButton":"  >>  ","SkinLibrary":"oregonstate","SkinType":"MQ","Skin":"oregonstate","NewScoring":1,"PreferJFE":true}},\n\n'
	h2 += '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"SCO","PrimaryAttribute":"Scoring","SecondaryAttribute":null,"TertiaryAttribute":null,"Payload":{"ScoringCategories":[],"ScoringCategoryGroups":[],"ScoringSummaryCategory":null,"ScoringSummaryAfterQuestions":0,"ScoringSummaryAfterSurvey":0,"DefaultScoringCategory":null,"AutoScoringCategory":null}},\n\n'
	h2 += '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"STAT","PrimaryAttribute":"Survey Statistics","SecondaryAttribute":null,"TertiaryAttribute":null,"Payload":{"MobileCompatible":true,"ID":"Survey Statistics"}},\n\n'
	h2 += '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"QC","PrimaryAttribute":"Survey Question Count","SecondaryAttribute":"'
	h2 += str(surveycount)
	h2 += '","TertiaryAttribute":null,"Payload":null},\n\n'
	h2 += '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"RS","PrimaryAttribute":"RS_3ydDuuDeA5tnma9","SecondaryAttribute":"Default Response Set","TertiaryAttribute":null,"Payload":null},\n\n'
	h2 += '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"SG","PrimaryAttribute":"SGRP_bvmgXN5j5CZS7NH","SecondaryAttribute":"RP_bvmgXN5j5CZS7NH","TertiaryAttribute":"RP_bvmgXN5j5CZS7NH","Payload":{"0":[{"LogicType":"Question","LeftOperand":"q:\/\/QID1\/SelectableChoice\/1","ChoiceLocator":"q:\/\/QID1\/SelectableChoice\/1","QuestionID":"QID1","Operator":"Selected","Type":"Expression","Description":"Question - Which given shape would take the longest to draw?<em>,<\/em> Choice - <em>,<\/em> <b>Is<\/b> Selected"}],"Type":"BooleanExpression","Name":"RP_bvmgXN5j5CZS7NH","LogicID":"SGRP_bvmgXN5j5CZS7NH"}},\n\n'
	return h2

def makeQuestion(surveycount, qtype, HeadList, qnum, img1, img2, img3):
	HeadList[qtype].append(qnum)
	surveycount += 1
	if qtype == draw:
		q = makeDrawQ(qnum, img1, img2)
	elif qtype == trace:
		q = makeTraceQ(qnum, img1, img2, img3)
	elif qtype == scissor:
		q = makeScissorQ(qnum, img1, img2, img3)
	q += '\n\n'
	return q, surveycount

def makeTraceQ(qnum, img1, img2, img3):
	q  = '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"SQ","PrimaryAttribute":"'
	q += 'QID' + str(qnum)
	q +=  '","SecondaryAttribute":"Which given shape would take the longest to trace?",'
	q += '"TertiaryAttribute":null,"Payload":{"QuestionText":"Which given shape would take the longest to trace?","DataExportTag":"'
	q += 'Q' + str(qnum)
	q += '","QuestionType":"MC","Selector":"SAHR","SubSelector":"TX","Configuration":{"QuestionDescriptionOption":"UseText","LabelPosition":"BELOW"},"QuestionDescription":"Which given shape would take the longest to trace?",'
	q += '"Choices":{"1":{"Display":"","Image":{"Display":"' + img1[0] + '","ImageLocation":"' + img1[1] + '"}},'
	q += '"2":{"Display":"","Image":{"Display":"' + img2[0] + '","ImageLocation":"' + img2[1] + '"}},'
	q += '"3":{"Display":"","Image":{"Display":"' + img3[0] + '","ImageLocation":"' + img3[1] + '"}}},'
	q += '"ChoiceOrder":["1","2","3"],"Validation":{"Settings":{"ForceResponse":"OFF","ForceResponseType":"ON","Type":"None"}},"Language":[],"QuestionID":"'
	q += 'QID' + str(qnum) + '"}},'
	return q

def makeDrawQ(qnum, img1, img2):
	q = '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"SQ","PrimaryAttribute":"'
	q += 'QID' + str(qnum)
	q += '","SecondaryAttribute":"Which given shape would take the longest to draw?",'
	q += '"TertiaryAttribute":null,"Payload":{"QuestionText":"Which given shape would take the longest to draw?","DataExportTag":"'
	q += 'Q' + str(qnum)
	q += '","QuestionType":"MC","Selector":"SAHR","SubSelector":"TX","Configuration":{"QuestionDescriptionOption":"UseText","LabelPosition":"BELOW"},"QuestionDescription":"Which given shape would take the longest to draw?",'
	q += '"Choices":{"1":{"Display":"","Image":{"Display":"' + img1[0] + '","ImageLocation":"'+ img1[1] + '"}},'
	q += '"2":{"Display":"","Image":{"Display":"' + img2[0] + '","ImageLocation":"' + img2[1] + '"}}},'
	q += '"ChoiceOrder":[1,2],"Validation":{"Settings":{"ForceResponse":"OFF","ForceResponseType":"ON","Type":"None"}},"Language":[],"QuestionID":"'
	q += 'QID' + str(qnum)
	q += '"}},'
	return q

def makeScissorQ(qnum, img1, img2, img3):
	q = '{"SurveyID":"SV_6WMJjyJENCW4L6l","Element":"SQ","PrimaryAttribute":"'
	q += 'QID' + str(qnum)
	q += '","SecondaryAttribute":"Which given shape would take the longest to cut out with scissors?",'
	q += '"TertiaryAttribute":null,"Payload":{"QuestionText":"Which given shape would take the longest to cut out with scissors?\\n<div trace=\\"text-align: center;\\">'
	q += '<img src=\\"' + img1[1] + '\\"><\/div>","DataExportTag":"'
	q += 'Q' + str(qnum)
	q += '","QuestionType":"MC","Selector":"SAHR","SubSelector":"TX","Configuration":{"QuestionDescriptionOption":"UseText","LabelPosition":"BELOW"},"QuestionDescription":"Which given shape would take the longest to cut out with scissors?",'
	q += '"Choices":{"1":{"Display":"","Image":{"Display":"' + img2[0] + '","ImageLocation":"' + img2[1] + '"}},'
	q += '"2":{"Display":"","Image":{"Display":"' + img3[0] + '","ImageLocation":"' + img3[1] + '"}}},'
	q += '"ChoiceOrder":[1,2],"Validation":{"Settings":{"ForceResponse":"OFF","ForceResponseType":"ON","Type":"None"}},"Language":[],"QuestionID":"'
	q += 'QID' + str(qnum)
	q += '"}},'
	return q

def end(str_val):
	str_val = str_val[:-3]
	str_val += ']}'
	return str_val

def img(pic, bas):
	pictures = ['boy', 'brushpainting', 'cat', 'dolphin', 'elephant', 'hat', 'mountains', 'seattle']
	bases = ['haar', 'hat', 'hermite', 'laguerre', 'scissorinal', 'pwl', 'quad', 'quads', 'sin']

	picname = pictures[pic] + '_' + bases[bas] + '.jpg'
	url = 'http://web.engr.oregonstate.edu/~grimmc/Images/' + pictures[pic] + '/' + picname

	return picname, url

if __name__ == "__main__":
	main()