/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - 003placement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`003placement` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `003placement`;

/*Table structure for table `applycmp` */

DROP TABLE IF EXISTS `applycmp`;

CREATE TABLE `applycmp` (
  `applyId` int(255) NOT NULL auto_increment,
  `cmpName` varchar(255) NOT NULL,
  `Jobtitle` varchar(255) NOT NULL,
  `resume` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `cat1` varchar(255) default 'Unavailable',
  `cat2` varchar(255) default 'Unavailable',
  `cat3` varchar(255) default 'Unavailable',
  `cat4` varchar(255) default 'Unavailable',
  `cat5` varchar(255) default 'Unavailable',
  `cat6` varchar(255) default 'Unavailable',
  `cat7` varchar(255) default 'Unavailable',
  `cat8` varchar(255) default 'Unavailable',
  `cat9` varchar(255) default 'Unavailable',
  `ques1` longtext,
  `ques2` longtext,
  `ques3` longtext,
  `ques4` longtext,
  `ques5` longtext,
  `status` varchar(255) NOT NULL default '',
  PRIMARY KEY  (`applyId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `applycmp` */

insert  into `applycmp`(`applyId`,`cmpName`,`Jobtitle`,`resume`,`fname`,`lname`,`cat1`,`cat2`,`cat3`,`cat4`,`cat5`,`cat6`,`cat7`,`cat8`,`cat9`,`ques1`,`ques2`,`ques3`,`ques4`,`ques5`,`status`) values (1,'asfaf','aHSdvhjads','static/upload_resume/05_IUSS_kn4_2018.pdf','Vedansh','Kapoor','mumbai','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','kafajdf','Not needed','Not needed','Not needed','Not needed','Selected'),(2,'ASHFSFH','askfksf','static/upload_resume/10.1109ICCCT2.2019.8824930.pdf','Vedansh','Kapoor','Punjab','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','ajgagakh','Not needed','Not needed','Not needed','Not needed','applied'),(3,'vbvbvb','vbvbv','static/upload_resume/10.1007s11277-020-07041-7.pdf','Vedansh','Kapoor','Vedansh','Kapoor','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','ajhdah','Not needed','Not needed','Not needed','Not needed','applied');

/*Table structure for table `botqa` */

DROP TABLE IF EXISTS `botqa`;

CREATE TABLE `botqa` (
  `QAid` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `question` longtext,
  `answers` longtext,
  PRIMARY KEY  (`QAid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `botqa` */

insert  into `botqa`(`QAid`,`username`,`question`,`answers`) values (72,'s','What is meant by the term OOPs?','OOPs refers to Object-Oriented Programming. It is the programming paradigm that is defined using objects. Objects can be considered as real-world instances of entities like class, that have some characteristics and behaviors'),(73,'s','What are the main features of OOPs?',' Inheritance Encapsulation Polymorphism Data Abstraction'),(74,'s','What is encapsulation?','One can visualize Encapsulation as the method of putting everything that is required to do the job, inside a capsule and presenting that capsule to the user. What it means is that by Encapsulation, all the necessary data and methods are bind together and all the unnecessary details are hidden to the normal user. So Encapsulation is the process of binding data members and methods of a program together to do a specific job, without revealing unnecessary details.'),(75,'s','What is Polymorphism?','In OOPs, Polymorphism refers to the process by which some code, data, method, or object behaves differently under different circumstances or contexts. Compile-time polymorphism and Run time polymorphism are the two types of polymorphisms in OOPs languages.'),(76,'s','What is meant by Inheritance?','The term â€œinheritanceâ€ means â€œreceiving some quality or behavior from a parent to an offspring.â€ In object-oriented programming, inheritance is the mechanism by which an object or class (referred to as a child) is created using the definition of another object or class (referred to as a parent). Inheritance not only helps to keep the implementation simpler but also helps to facilitate code reuse.'),(77,'s','What is Abstraction?','If you are a user, and you have a problem statement, you don\'t want to know how the components of the software work, or how it\'s made. You only want to know how the software solves your problem. Abstraction is the method of hiding unnecessary details from the necessary ones. It is one of the main features of OOPs.'),(78,'s','What is a constructor?','Constructors are special methods whose name is the same as the class name. The constructors serve the special purpose of initializing the objects.'),(79,'s','What is a destructor?','Contrary to constructors, which initialize objects and specify space for them, Destructors are also special methods. But destructors free up the resources and memory occupied by an object. Destructors are automatically called when an object is being destroyed.'),(80,'s','Are there any limitations of Inheritance?','Yes, with more powers comes more complications. Inheritance is a very powerful feature in OOPs, but it has some limitations too. Inheritance needs more time to process, as it needs to navigate through multiple classes for its implementation. Also, the classes involved in Inheritance - the base class and the child class, are very tightly coupled together. So if one needs to make some changes, they might need to do nested changes in both classes. Inheritance might be complex for implementation, as well. So if not correctly implemented, this might lead to unexpected errors or incorrect outputs'),(81,'s','What is a subclass?','The subclass is a part of Inheritance. The subclass is an entity, which inherits from another class. It is also known as the child class'),(82,'s','What is an interface?','An interface refers to a special type of class, which contains methods, but not their definition. Only the declaration of methods is allowed inside an interface. To use an interface, you cannot create objects. Instead, you need to implement that interface and define the methods for their implementation.'),(83,'s','Define a superclass?','Superclass is also a part of Inheritance. The superclass is an entity, which allows subclasses or child classes to inherit from itself.'),(84,'s','What is the difference between overloading and overriding?','Overloading is a compile-time polymorphism feature in which an entity has multiple implementations with the same name. For example, Method overloading and Operator overloading.'),(85,'s','What is an abstract class?','An abstract class is a special class containing abstract methods. The significance of abstract class is that the abstract methods inside it are not implemented and only declared. So as a result, when a subclass inherits the abstract class and needs to use its abstract methods, they need to define and implement them'),(86,'s','What is an exception?','An exception can be considered as a special event, which is raised during the execution of a program at runtime, that brings the execution to a halt. The reason for the exception is mainly due to a position in the program, where the user wants to do something for which the program is not specified, like undesirable input'),(87,'s','Can we run a Java application without implementing the OOPs concept?','No. Java applications are based on Object-oriented programming models or OOPs concept, and hence they cannot be implemented without it.'),(88,'s','What is Artificial Intelligence?','Artificial Intelligence (AI) is an area of computer science that emphasizes the creation of intelligent machines that work and react like humans.â€ â€œThe capability of a machine to imitate the intelligent human behavior'),(89,'s','What are the different types of AI?','Reactive Machines AI: Based on present actions, it cannot use previous experiences to form current decisions and simultaneously update their memory.\nExample: Deep Blue\nLimited Memory AI: Used in self-driving cars. They detect the movement of vehicles around them constantly and add it to their memory.\nTheory of Mind AI: Advanced AI that has the ability to understand emotions, people and other things in the real world.\nSelf Aware AI: AIs that posses human-like consciousness and reactions. Such machines have the ability to form self-driven actions.\nArtificial Narrow Intelligence (ANI): General purpose AI, used in building virtual assistants like Siri.\nArtificial General Intelligence (AGI): Also known as strong AI. An example is the Pillo robot that answers questions related to health.\nArtificial Superhuman Intelligence (ASI): AI that possesses the ability to do everything that a human can do and more. An example is the Alpha 2 which is the first humanoid ASI robot.'),(90,'s','What is Q-Learning?','The Q-learning is a Reinforcement Learning algorithm in which an agent tries to learn the optimal policy from its past experiences with the environment. The past experiences of an agent are a sequence of state-action-rewards'),(91,'s','What is Deep Learning?','Deep learning imitates the way our brain works i.e. it learns from experiences. It uses the concepts of neural networks to solve complex problems.'),(92,'s','Explain the assessment that is used to test the intelligence of a machine.','In artificial intelligence (AI), a Turing Test is a method of inquiry for determining whether or not a computer is capable of thinking like a human being.'),(93,'s','Why do we need Artificial Intelligence?','The goal of Artificial intelligence is to create intelligent machines that can mimic human behavior. We need AI for today\'s world to solve complex problems, make our lives more smoothly by automating the routine work, saving the manpower, and to perform many more other tasks.'),(94,'s','What are the different domains/Subsets of AI?','AI covers lots of domains or subsets, and some main domains are given below:\n\nMachine Learning\nDeep Learning\nNeural Network\nExpert System\nFuzzy Logic\nNatural Language Processing\nRobotics\nSpeech Recognition. Read More'),(95,'s','How is machine learning related to AI?','Machine learning is a subset or subfield of Artificial intelligence. It is a way of achieving AI. As both are the two different concepts and the relation between both can be understood as \"AI uses different Machine learning algorithms and concepts to solve the complex problems'),(96,'s','What do you understand by the reward maximization?','Reward maximization term is used in reinforcement learning, and which is a goal of the reinforcement learning agent. In RL, a reward is a positive feedback by taking action for a transition from one state to another. If the agent performs a good action by applying optimal policies, he gets a reward, and if he performs a bad action, one reward is subtracted. The goal of the agent is to maximize these rewards by applying optimal policies, which is termed as reward maximization.'),(97,'s','Explain the Hidden Markov model','Hidden Markov model is a statistical model used for representing the probability distributions over a chain of observations. In the hidden markov model, hidden defines a property that it assumes that the state of a process generated at a particular time is hidden from the observer, and Markov defines that it assumes that the process satisfies the Markov property. The HMM models are mostly used for temporal data.'),(98,'s','What is the use of computer vision in AI?','Computer vision is a field of Artificial Intelligence that is used to train the computers so that they can interpret and obtain information from the visual world such as images. Hence, computer vision uses AI technology to solve complex problems such as image processing, object detections, etc.'),(99,'s','What are the various techniques of knowledge representation in AI?','Knowledge representation techniques are given below:\n\nLogical Representation\nSemantic Network Representation\nFrame Representation\nProduction Rules'),(100,'s','Which programming language is not generally used in AI, and why?','Perl Programming language is not commonly used language for AI, as it is the scripting language.');

/*Table structure for table `botques` */

DROP TABLE IF EXISTS `botques`;

CREATE TABLE `botques` (
  `quesId` int(255) NOT NULL auto_increment,
  `username` varchar(255) default '',
  `answer` longtext,
  `botQues` longtext,
  PRIMARY KEY  (`quesId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `botques` */

insert  into `botques`(`quesId`,`username`,`answer`,`botQues`) values (7,'s','yes',NULL);

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `id` int(255) NOT NULL auto_increment,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `mob` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`id`,`fname`,`lname`,`mob`,`email`,`pass`,`role`) values (1,'abc','xyz','9856321470','a@gmail.com','a','Computer science'),(2,'xyz','abc','0987654321','x@gmail.com','x','Electronics');

/*Table structure for table `deadline_over` */

DROP TABLE IF EXISTS `deadline_over`;

CREATE TABLE `deadline_over` (
  `jobId` int(255) NOT NULL auto_increment,
  `companyName` varchar(255) NOT NULL,
  `logo` longtext NOT NULL,
  `jobTitle` varchar(255) NOT NULL,
  `jobLoc` varchar(255) NOT NULL,
  `jobType` varchar(255) NOT NULL,
  `publishedOn` varchar(255) NOT NULL,
  `Salary` varchar(255) NOT NULL,
  `ApplicationDeadline` varchar(255) NOT NULL,
  `JobDescription` longtext NOT NULL,
  `Responsibilities` longtext NOT NULL,
  `Education_Experience` longtext NOT NULL,
  `OtherBenifits` longtext NOT NULL,
  `uname` varchar(255) NOT NULL,
  `branches` varchar(255) NOT NULL,
  `studentInfo` longtext,
  `desc1` longtext,
  `desc2` longtext,
  `desc3` longtext,
  `desc4` longtext,
  `desc5` longtext,
  `ques1` longtext,
  `ques2` longtext,
  `ques3` longtext,
  `ques4` longtext,
  `ques5` longtext,
  PRIMARY KEY  (`jobId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `deadline_over` */

insert  into `deadline_over`(`jobId`,`companyName`,`logo`,`jobTitle`,`jobLoc`,`jobType`,`publishedOn`,`Salary`,`ApplicationDeadline`,`JobDescription`,`Responsibilities`,`Education_Experience`,`OtherBenifits`,`uname`,`branches`,`studentInfo`,`desc1`,`desc2`,`desc3`,`desc4`,`desc5`,`ques1`,`ques2`,`ques3`,`ques4`,`ques5`) values (1,'Apple','../static/logo/apple.jpg','software developer','Delhi','Intern','2022-09-07','15LPA','2022-09-16','jadfsfbbfs','jhdgfjshdf','kdfiu','jadgsj','abc','Computer science','[\'fname\', \'lname\', \'Hometown\', \'achivmnt\', \'clgname\', \'percent12\']','Not needed','Not needed','Not needed','Not needed','Not needed','Not needed','Not needed','Not needed','Not needed','Not needed'),(4,'safgfg','../static/logo/Honeywell-Logo.png','sas','asgfasg','sasgf','2022-09-15','asgfasg','2022-09-16','safgfg','asfgfg','asfgasfg','asfgasfg','abc','Computer science','[\'fname\', \'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','sagasfg','Not needed','Not needed','Not needed','Not needed'),(5,'asass','../static/logo/siemens.jpg','aaaa','asasa','asdasas','2022-09-15','asass','2022-09-16','asasas','asass','asasa','asas','abc','Computer science','[\'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','asasas','Not needed','Not needed','Not needed','Not needed'),(6,'qwqww','../static/logo/siemens.jpg','asas','qwqw','asqwqw','2022-09-15','qwqwqw','2022-09-16','qwqwq','qwqw','qwq','qqwqw','abc','Computer science','[\'fname\']','Not needed','Not needed','Not needed','Not needed','Not needed','qwqww','Not needed','Not needed','Not needed','Not needed'),(7,'akjfadkjf','../static/logo/Honeywell-Logo.png','ahjsdadh','jdgjasd','aghjahd','2022-09-15','jadgsjas','2022-09-16','jagjahsdg','kajakdf','kfak','kaakdj','abc','Electronics ','[\'fname\', \'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','akjsajsd','Not needed','Not needed','Not needed','Not needed'),(9,'HKHJ','../static/logo/havells.png','ASDADAS','HKJHJ','HKHKK','2022-09-15','HHKK','2022-09-16','HKHKHK','HJKJKHK','HKHKJ','HJKHK','abc','Computer science','[\'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','HJKHK','Not needed','Not needed','Not needed','Not needed'),(10,'YUYYU','../static/logo/godreg.png','YYUYUY','YUYU','YUYUU','2022-09-15','YUY','2022-09-15','YUYUU','YUUY','YUY','YUYU','abc','Computer science','[\'lname\', \'fathername\']','Not needed','Not needed','Not needed','Not needed','Not needed','YYUYU','Not needed','Not needed','Not needed','Not needed'),(11,'opopo','../static/logo/tsls.JPG','opopopop','opop','opopo','2022-09-15','opopo','2022-09-16','opopop','opopo','opop','opo','abc','Computer science','[\'fname\', \'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','opopo','Not needed','Not needed','Not needed','Not needed'),(12,'ririi','../static/logo/tsls.JPG','riririr','ririi','riiriri','2022-09-15','rriri','2022-09-15','ririrri','rriii','riri','ririi','abc','Computer science','[\'fname\', \'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','ririi','Not needed','Not needed','Not needed','Not needed');

/*Table structure for table `jobinfo` */

DROP TABLE IF EXISTS `jobinfo`;

CREATE TABLE `jobinfo` (
  `jobId` int(255) NOT NULL auto_increment,
  `companyName` varchar(255) NOT NULL,
  `logo` longtext NOT NULL,
  `jobTitle` varchar(255) NOT NULL,
  `jobLoc` varchar(255) NOT NULL,
  `jobType` varchar(255) NOT NULL,
  `publishedOn` varchar(255) NOT NULL,
  `Salary` varchar(255) NOT NULL,
  `ApplicationDeadline` varchar(255) NOT NULL,
  `JobDescription` longtext NOT NULL,
  `Responsibilities` longtext NOT NULL,
  `Education_Experience` longtext NOT NULL,
  `OtherBenifits` longtext NOT NULL,
  `uname` varchar(255) NOT NULL,
  `branches` varchar(255) NOT NULL,
  `studentInfo` longtext,
  `desc1` longtext,
  `desc2` longtext,
  `desc3` longtext,
  `desc4` longtext,
  `desc5` longtext,
  `ques1` longtext,
  `ques2` longtext,
  `ques3` longtext,
  `ques4` longtext,
  `ques5` longtext,
  PRIMARY KEY  (`jobId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `jobinfo` */

insert  into `jobinfo`(`jobId`,`companyName`,`logo`,`jobTitle`,`jobLoc`,`jobType`,`publishedOn`,`Salary`,`ApplicationDeadline`,`JobDescription`,`Responsibilities`,`Education_Experience`,`OtherBenifits`,`uname`,`branches`,`studentInfo`,`desc1`,`desc2`,`desc3`,`desc4`,`desc5`,`ques1`,`ques2`,`ques3`,`ques4`,`ques5`) values (2,'asfaf','../static/logo/accenture.png','aHSdvhjads','asdah','as','2022-09-09','asd','2022-09-30','afadf','dsgfa','asfgs','asfgfg','abc','Computer science','[\'fname\', \'lname\']','jahdfvakfjvajsf asdgfkasdf sadgfksjfg','Not needed','Not needed','Not needed','Not needed','Enter your name','Not needed','Not needed','Not needed','Not needed'),(3,'Godrej','../static/logo/godreg.png','Interior Designer','Mumbai','Intern','2022-09-10','10LPA','2022-10-29','1) Meeting Architects and clients for discussions and qualitative suggestions pertaining to interior works.\r\n\r\n2) Understanding customer needs qualitatively and quantitatively.\r\n\r\n3) Prompt response to customers in terms of queries pertaining to design.\r\n\r\n4) Recommending cost variable options with in specified budget range in terms of :- a) Layout design b) Furniture systems c) Material specifications.\r\n\r\n5) Preparing presentations for client and architects.\r\n\r\n6) Working out the best possible design option and costing for the project.','1) Meeting Architects and clients for discussions and qualitative suggestions pertaining to interior works.\r\n\r\n2) Understanding customer needs qualitatively and quantitatively.','B.Sc, B.Arch in Architecture, Diploma in Architecture, Fashion Designing/Other Designing, B.Des. in Furniture Design','Travel allowance, food facility','abc','Electronics ','[\'fname\', \'lname\', \'phnno\', \'brnch\', \'cgpa\', \'percent10\']','Godrej Interio is Indias premium furniture brand in both home and institutional segments with a strong commitment to sustainability and centers of excellence in design, manufacturing and retail. With presence in over 430 cities with 52 company owned stores and over 800 dealers, Godrej Interio is one of the largest business of Godrej and Boyce Mfg. Co. Ltd.\r\nLed by the largest in-house design team in the country in the furniture category and awarded with 34 India Design Mark Awards till date, Godrej Interio aims to transform spaces with its thoughtfully designed furniture to create brighter homes and offices with products that have the highest design quotient in aesthetics, functionality and technology. With consistent pursuit of excellence and a special focus on health and ergonomics, the product portfolio of Godrej Interio comprises a massive range in the home, office and other specialized applications.\r\nThe brand boasts of noteworthy awards received so far- CII Exim Bank Award for Business Excellence 2016, Asias most admired brand 2016, Superbrands 2017-18, Reader’s Digest Most Trusted Brand 2018 Gold (Home Furniture) and Reader’s Digest Most Trusted Brand 2018 Gold (Modular Kitchens). www.godrejinterio.com','Not needed','Not needed','Not needed','Not needed','What are the skills you have?','Not needed','Not needed','Not needed','Not needed'),(8,'ASHFSFH','../static/logo/siemens.jpg','askfksf','AKFGA','AGFADGF','2022-09-15','AGFA','2022-09-27','IASDFUASF','AFKHGADFK','KAUGFF','AASDAKS','abc','Computer science','[\'curntLoc\']','Not needed','Not needed','Not needed','Not needed','Not needed','KAJFBADF','Not needed','Not needed','Not needed','Not needed'),(13,'vbvbvb','../static/logo/e.png','vbvbv','bvbv','vbvbv','2022-09-16','vbvb','2022-09-17','bvvbvbv','vbvb','vbvb','vbvb','abc','Computer science','[\'fname\', \'lname\']','Not needed','Not needed','Not needed','Not needed','Not needed','vbvbvb','Not needed','Not needed','Not needed','Not needed');

/*Table structure for table `studentinfo` */

DROP TABLE IF EXISTS `studentinfo`;

CREATE TABLE `studentinfo` (
  `studId` int(255) NOT NULL auto_increment,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `fathername` varchar(255) NOT NULL,
  `mothername` varchar(255) NOT NULL,
  `curntLoc` varchar(255) NOT NULL default '',
  `Hometown` varchar(255) NOT NULL default '',
  `certif` varchar(255) NOT NULL default '',
  `cgpa` varchar(255) NOT NULL default '',
  `clgname` varchar(255) NOT NULL,
  `rolno` varchar(255) NOT NULL,
  `cEmail` varchar(255) NOT NULL,
  `pEmail` varchar(255) NOT NULL,
  `phnno` varchar(255) NOT NULL,
  `brnch` varchar(255) NOT NULL,
  `degre` varchar(255) NOT NULL,
  `percent10` varchar(255) NOT NULL,
  `percent12` varchar(255) NOT NULL,
  `actbacklog` varchar(255) NOT NULL,
  PRIMARY KEY  (`studId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `studentinfo` */

insert  into `studentinfo`(`studId`,`fname`,`lname`,`fathername`,`mothername`,`curntLoc`,`Hometown`,`certif`,`cgpa`,`clgname`,`rolno`,`cEmail`,`pEmail`,`phnno`,`brnch`,`degre`,`percent10`,`percent12`,`actbacklog`) values (1,'Vedansh','Kapoor','abc','mnb','Punjab','Punjab','Java,Python','8.8900000000000006','ABC collage of engineering','1CS523832','v@gmail.com','vedansh@gmail.com','9856321470','Computer Science','B.E','80','85','0'),(2,'Manan','Sodhi','def','lkj','Hyderabad','Hyderabad','Flutter,Java','8.5600000000000005','ABC collage of engineering','1CS523833','man@gmail.com','manan@gmail.com','9896321443','Electronics','B.E','90','90','1');

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `id` int(255) NOT NULL auto_increment,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `mob` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`id`,`fname`,`lname`,`mob`,`email`,`pass`,`Department`) values (1,'Vedansh','Kapoor','9856321470','v@gmail.com','v','Computer Science'),(2,'Manan','Sodhi','9896321443','man@gmail.com','man','Electronics');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
