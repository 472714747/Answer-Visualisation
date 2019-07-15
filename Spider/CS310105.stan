<?xml version="1.0"?>
<!DOCTYPE answerPaper SYSTEM "answer.dtd">
<!-- serialize from mancs.caa.core at Thu Jan 19 11:48:27 GMT 2006 -->
<answerPaper studentId="SAMPLESANSWER" examId="CS310105" timeTaken="0" allImages="true">
	<compositea marksAwarded="100" isMarked="true">
		<compositea marksAwarded="20" isMarked="true">
			<freeTextAnswer marksAwarded="4" isMarked="true">
				<answerString>
					Firstly, in spite of the pun, Rooney is an instance, not a class (and I hope Man U’s
					form has picked up by January otherwise I’m going to look rather silly!).
					
					Otherwise this is a classic roles example. Different players may play different roles
					at different times etc. A delegation solution e.g.
					
					public class Footballer {
					private Position currentPosition;
					}
					
					is better. Whether there should be separate classes for separate positions depends on
					the context.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="4" isMarked="true">
				<answerString>
					Implementation inheritance, bad for all the standard reasons, should delegate.
					A discussion  of how things might be different in Java 1.5 is ok for 1
					mark, but not required.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="4" isMarked="true">
				<answerString>
					It’s possible to make the argument for MI here, as the superclasses are reasonably disjoint,
					and the common biis (e.g. power) can go in the PersonalElectronicEquiplemnt class.
					The usual issues about name clashes etc. apply, and CameraPhone doesn’t sound like a
					cohesive class. The main argument against is extensibility – where would a PDA etc. fit in?
					
					Marks for any sensible solution, the most obvious being:
					-	consider it primarily as a phone and delegate to the other functions
					-	consider it as a completely modular thing where phone, camera, PDA etc.
					are all treated separately and uniformly.
				</answerString>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="4" isMarked="true">
				<answerString>
					In principle this is a reasonable use of MI as it’s
					combining disjoint behaviours. However, this requires that the language has
					MI and some way of implementing the default copy() (in Java this can only be done
					directly in the language via reflection). Alternatives are to treat copying as a special c
					ase and build it in (as in C++), or to make copy() abstract, so Copyable can be an i
					nterface, or make Copyable a marker interface and build a default copy() into class
					Object, which is what Java actually does with clone().
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="4" isMarked="true">
				<answerString>
					This is the actual design of the system, so clearly it’s correct!
					The Answer classes and the first two subclasses are obviously fine.
					The NoAnswerProvided class is an example of the Null Object pattern, as is
					useful as you need to see clearly where students have failed to answer a part-question.
					NoAnswerRequired is more debatable. It does fit with the rest of the structure, and in
					particular is useful for distinguishing this case from the previous one, but it’s not strictly
					necessary. The could also get a mark for pointing out the need for a CompositeAnswer class –
					which is there but not shown in the question,
					so the whole thing is an example of the Composite pattern.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
		</compositea>
		<compositea marksAwarded="20" isMarked="true">
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					General stuff about making things private to separate interface and implementation etc
					. Any reasonable example is fine.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					The point here is that grubby code introduced for performance reasons can be hidden –
					or switched in and out – via encapsulation.
					The example in the lectures was different implementations of a complex vector class.
				</answerString>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					The idea is to treat pointers within a class and ones outside it separately.
					The example used in the course is a stack implemented using a linked list.
					Any example of a dynamic data structure encapsulated within a class is fine.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					This is not explicitly stated in the course, but since preconditions etc.
					are part of the interface of a class, they should be unchanged by different
					implementations, and breaking encapsulation is not consistent with DBC –
					we need to specify the constraints on each class separately. A lift (which
					can be restricted to specific floors, min to max)
					is my favourite example, but marks for anything reasonable.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
		</compositea>
		<compositea marksAwarded="20" isMarked="true">
			<freeTextAnswer marksAwarded="2" isMarked="true">
				<answerString>
					&quot;A pattern of communicating classes and/or objects which can be customised to
					solve a general design problem in a specific context.&quot;
					
					Precise definition or close paraphrase required for 2 marks. Right general idea, 1 mark.
				</answerString>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="6" isMarked="true">
				<answerString>
					This has been discussed in the lectures, so a good coherent explanation is required for full marks.
					
					Composite allows us to build a tree stucture in which all branches and leaves can be
					treated uniformly, by dynamic binding. For .e.g. questions, it would look like:
					
					public abstract class Question {
					
					// Example method
					public abstract int getMarksAllocated();
					}
					
					// A leaf, with a fixed number of marks
					public abstract class AtomicQuestiion extends Question {
					private int marksAllocated;
					
					public int getMarksAllocated() { return marksAllocated; }
					}
					
					// MCQ, text question etc. extend AtomicQuestion
					
					// A question which contains subquestions
					public class CompositeQuestion extends Question {
					private Question[] subquestions;
					
					public int getMarksAllocated() {
					// Add up the marks of all the subquestions
					... subQuestions[i].getMarksAllocated(); // Recursion and dynamic binding.
					}
					}
					
					They don&apos;t necessarily have to express it in code like this, but a full and precise description
					in some form is necessary.
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="12" isMarked="true">
				<answerString>
					Any 4 explained coherently, e.g.
					
					A GUI is required, so Observer would apply - in Java this would take the form of the
					delegation event model - event listenders registering with event sources and being
					notified when events occur etc. Observer could also be used to register exam clients
					with the server (that&apos;s more or less what we do).
					
					Null object for null answers –  c.f. Q1.5. Representing unswered part-questions as objects
					rather than as nulls would enable all answers to be treated uniformly by dynamic binding,
					e.g. we could include them in a method to add up marks by just having them return 0.
					Otherwise all such methods would have to explicitly check for null all the time, which would
					be a hell of a mess.
					
					Strategy for marking strategies. A sophisticated marking tool (the one we&apos;ll have next
					year :-) would need to have a variety of stategies for helping the human marker which
					would be decided at runtime (e.g. by the marker selecting them). Hence the Strategy
					pattern, treating a marking strategy as an object of a subclass of an abstract MarkingStrategy
					class might well be applicable.
					
					Singleton for the server. We might want to ensure that there was only one instance of the
					server class, and enforce this using the Singlton Pattern.
					
					No doubt they&apos;ll come up with lots of other suggestions, pretty well any pattern could be
					applicable. For the full three marks they should say what the pattern is clearly enough
					that you get the idea, and be specific about how it applies in this application.
				</answerString>
			</freeTextAnswer>
		</compositea>
		<compositea marksAwarded="20" isMarked="true">
			<compositea marksAwarded="15" isMarked="true">
				<freeTextAnswer marksAwarded="5" isMarked="true">
					<answerString>
						a)	The purpose of contracts is to specify clearly the obligations and rights of each class and its
						lients. The obligation for a class is to guarantee its behaviour (functionality) whenever it is used in the specified
						way. Its right is to expect the client to observe the usage condition. The obligation for a client is to observe the
						usage condition. Its right is to expect the class to deliver the guaranteed functionality. By making clients and
						suppliers share the obligations (clearly specified by their contracts), we can use contracts for developing
						reliable software.                                                                                   (3 marks)
						
						Contracts can be defined by pre- and post-conditions for methods, and invariants for classes.
						(2 marks)
					</answerString>
					<feedback>
						&lt;html&gt;
						&lt;head&gt;
						
						&lt;/head&gt;
						&lt;body&gt;
						&lt;p style=&quot;margin-top: 0&quot;&gt;
						
						&lt;/p&gt;
						&lt;/body&gt;
						&lt;/html&gt;
					</feedback>
				</freeTextAnswer>
				<freeTextAnswer marksAwarded="10" isMarked="true">
					<answerString>
						b)	For SqRoot:
						Need method for calculating the square root, with
						pre: number inout is non-negative
						post: result is the square root of the number input                                (2 marks)
						
						For Stack:
						Need methods for push, pop, etc:
						Push: pre: stack not full
						post: top of stack is new element
						Pop: pre: stack not empty
						post: top element is popped                                                         (4 marks)
						
						For the whole class, the invariant would be that the stack counter is non-negative, and the
						stack size does not exceed max size.                                   (2 marks)
						
						Good explanation.                                                                                             (2 marks)
					</answerString>
				</freeTextAnswer>
			</compositea>
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					Program calls SqRoot on each number in Stack.                                              (3 marks)
					
					Benefits are that the program can rely on SqRoot and Stack being
					correct, provided it calls their methods according to their pre-conditions.                                      (2 marks)
				</answerString>
			</freeTextAnswer>
		</compositea>
		<compositea marksAwarded="20" isMarked="true">
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					A software component is a block of software that has encapsulation, has an
					interface, is replaceable, reusable and inter-operable, etc. Examples: modules, classes, etc.
					(5 marks)
				</answerString>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="10" isMarked="true">
				<answerString>
					Need to use a database to store the up-to-date book stock.                                (1 mark)
					
					Need to use an entity bean to keep the stock up-to-date, and to allow the user clients to browse the stock.
					(2 marks)
					
					Need to use (two) session beans for the librarian client to record issues and returns.      (2 marks)
					
					Sketch of entity bean (home interface, remote interface, methods).                (2 marks)
					
					Sketch of session beans, one for issues, one for returns (home interface, remote interface, methods).
					(5 marks)
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
			<freeTextAnswer marksAwarded="5" isMarked="true">
				<answerString>
					Composition of Java beans only provides event handling. Java beans do not provide a facility to interact with a
					data base, like an entity bean in EJB, which the
					ibrary system requires, to store the up-to-date record of available books.                  (5 marks)
				</answerString>
				<feedback>
					&lt;html&gt;
					&lt;head&gt;
					
					&lt;/head&gt;
					&lt;body&gt;
					&lt;p style=&quot;margin-top: 0&quot;&gt;
					
					&lt;/p&gt;
					&lt;/body&gt;
					&lt;/html&gt;
				</feedback>
			</freeTextAnswer>
		</compositea>
	</compositea>
</answerPaper>
