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
  `cat1` varchar(255) default NULL,
  `cat2` varchar(255) default NULL,
  `cat3` varchar(255) default NULL,
  `cat4` varchar(255) default NULL,
  `cat5` varchar(255) default NULL,
  `cat6` varchar(255) default NULL,
  `cat7` varchar(255) default NULL,
  `cat8` varchar(255) default NULL,
  `cat9` varchar(255) default NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY  (`applyId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `applycmp` */

LOCK TABLES `applycmp` WRITE;

insert  into `applycmp`(`applyId`,`cmpName`,`Jobtitle`,`resume`,`fname`,`lname`,`cat1`,`cat2`,`cat3`,`cat4`,`cat5`,`cat6`,`cat7`,`cat8`,`cat9`,`status`) values (1,'Apple','software developer','static/upload_resume/New_Product_Launch.pdf','sanika','kadam','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','applied'),(2,'Microsoft','software developer','static/upload_resume/Madhav_Resume_1.pdf','Vedansh','Kapoor','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','Unavailable','applied');

UNLOCK TABLES;

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

LOCK TABLES `botqa` WRITE;

insert  into `botqa`(`QAid`,`username`,`question`,`answers`) values (72,'s','What is meant by the term OOPs?','OOPs refers to Object-Oriented Programming. It is the programming paradigm that is defined using objects. Objects can be considered as real-world instances of entities like class, that have some characteristics and behaviors'),(73,'s','What are the main features of OOPs?',' Inheritance Encapsulation Polymorphism Data Abstraction'),(74,'s','What is encapsulation?','One can visualize Encapsulation as the method of putting everything that is required to do the job, inside a capsule and presenting that capsule to the user. What it means is that by Encapsulation, all the necessary data and methods are bind together and all the unnecessary details are hidden to the normal user. So Encapsulation is the process of binding data members and methods of a program together to do a specific job, without revealing unnecessary details.'),(75,'s','What is Polymorphism?','In OOPs, Polymorphism refers to the process by which some code, data, method, or object behaves differently under different circumstances or contexts. Compile-time polymorphism and Run time polymorphism are the two types of polymorphisms in OOPs languages.'),(76,'s','What is meant by Inheritance?','The term â€œinheritanceâ€ means â€œreceiving some quality or behavior from a parent to an offspring.â€ In object-oriented programming, inheritance is the mechanism by which an object or class (referred to as a child) is created using the definition of another object or class (referred to as a parent). Inheritance not only helps to keep the implementation simpler but also helps to facilitate code reuse.'),(77,'s','What is Abstraction?','If you are a user, and you have a problem statement, you don\'t want to know how the components of the software work, or how it\'s made. You only want to know how the software solves your problem. Abstraction is the method of hiding unnecessary details from the necessary ones. It is one of the main features of OOPs.'),(78,'s','What is a constructor?','Constructors are special methods whose name is the same as the class name. The constructors serve the special purpose of initializing the objects.'),(79,'s','What is a destructor?','Contrary to constructors, which initialize objects and specify space for them, Destructors are also special methods. But destructors free up the resources and memory occupied by an object. Destructors are automatically called when an object is being destroyed.'),(80,'s','Are there any limitations of Inheritance?','Yes, with more powers comes more complications. Inheritance is a very powerful feature in OOPs, but it has some limitations too. Inheritance needs more time to process, as it needs to navigate through multiple classes for its implementation. Also, the classes involved in Inheritance - the base class and the child class, are very tightly coupled together. So if one needs to make some changes, they might need to do nested changes in both classes. Inheritance might be complex for implementation, as well. So if not correctly implemented, this might lead to unexpected errors or incorrect outputs'),(81,'s','What is a subclass?','The subclass is a part of Inheritance. The subclass is an entity, which inherits from another class. It is also known as the child class'),(82,'s','What is an interface?','An interface refers to a special type of class, which contains methods, but not their definition. Only the declaration of methods is allowed inside an interface. To use an interface, you cannot create objects. Instead, you need to implement that interface and define the methods for their implementation.'),(83,'s','Define a superclass?','Superclass is also a part of Inheritance. The superclass is an entity, which allows subclasses or child classes to inherit from itself.'),(84,'s','What is the difference between overloading and overriding?','Overloading is a compile-time polymorphism feature in which an entity has multiple implementations with the same name. For example, Method overloading and Operator overloading.'),(85,'s','What is an abstract class?','An abstract class is a special class containing abstract methods. The significance of abstract class is that the abstract methods inside it are not implemented and only declared. So as a result, when a subclass inherits the abstract class and needs to use its abstract methods, they need to define and implement them'),(86,'s','What is an exception?','An exception can be considered as a special event, which is raised during the execution of a program at runtime, that brings the execution to a halt. The reason for the exception is mainly due to a position in the program, where the user wants to do something for which the program is not specified, like undesirable input'),(87,'s','Can we run a Java application without implementing the OOPs concept?','No. Java applications are based on Object-oriented programming models or OOPs concept, and hence they cannot be implemented without it.'),(88,'s','What is Artificial Intelligence?','Artificial Intelligence (AI) is an area of computer science that emphasizes the creation of intelligent machines that work and react like humans.â€ â€œThe capability of a machine to imitate the intelligent human behavior'),(89,'s','What are the different types of AI?','Reactive Machines AI: Based on present actions, it cannot use previous experiences to form current decisions and simultaneously update their memory.\nExample: Deep Blue\nLimited Memory AI: Used in self-driving cars. They detect the movement of vehicles around them constantly and add it to their memory.\nTheory of Mind AI: Advanced AI that has the ability to understand emotions, people and other things in the real world.\nSelf Aware AI: AIs that posses human-like consciousness and reactions. Such machines have the ability to form self-driven actions.\nArtificial Narrow Intelligence (ANI): General purpose AI, used in building virtual assistants like Siri.\nArtificial General Intelligence (AGI): Also known as strong AI. An example is the Pillo robot that answers questions related to health.\nArtificial Superhuman Intelligence (ASI): AI that possesses the ability to do everything that a human can do and more. An example is the Alpha 2 which is the first humanoid ASI robot.'),(90,'s','What is Q-Learning?','The Q-learning is a Reinforcement Learning algorithm in which an agent tries to learn the optimal policy from its past experiences with the environment. The past experiences of an agent are a sequence of state-action-rewards'),(91,'s','What is Deep Learning?','Deep learning imitates the way our brain works i.e. it learns from experiences. It uses the concepts of neural networks to solve complex problems.'),(92,'s','Explain the assessment that is used to test the intelligence of a machine.','In artificial intelligence (AI), a Turing Test is a method of inquiry for determining whether or not a computer is capable of thinking like a human being.'),(93,'s','Why do we need Artificial Intelligence?','The goal of Artificial intelligence is to create intelligent machines that can mimic human behavior. We need AI for today\'s world to solve complex problems, make our lives more smoothly by automating the routine work, saving the manpower, and to perform many more other tasks.'),(94,'s','What are the different domains/Subsets of AI?','AI covers lots of domains or subsets, and some main domains are given below:\n\nMachine Learning\nDeep Learning\nNeural Network\nExpert System\nFuzzy Logic\nNatural Language Processing\nRobotics\nSpeech Recognition. Read More'),(95,'s','How is machine learning related to AI?','Machine learning is a subset or subfield of Artificial intelligence. It is a way of achieving AI. As both are the two different concepts and the relation between both can be understood as \"AI uses different Machine learning algorithms and concepts to solve the complex problems'),(96,'s','What do you understand by the reward maximization?','Reward maximization term is used in reinforcement learning, and which is a goal of the reinforcement learning agent. In RL, a reward is a positive feedback by taking action for a transition from one state to another. If the agent performs a good action by applying optimal policies, he gets a reward, and if he performs a bad action, one reward is subtracted. The goal of the agent is to maximize these rewards by applying optimal policies, which is termed as reward maximization.'),(97,'s','Explain the Hidden Markov model','Hidden Markov model is a statistical model used for representing the probability distributions over a chain of observations. In the hidden markov model, hidden defines a property that it assumes that the state of a process generated at a particular time is hidden from the observer, and Markov defines that it assumes that the process satisfies the Markov property. The HMM models are mostly used for temporal data.'),(98,'s','What is the use of computer vision in AI?','Computer vision is a field of Artificial Intelligence that is used to train the computers so that they can interpret and obtain information from the visual world such as images. Hence, computer vision uses AI technology to solve complex problems such as image processing, object detections, etc.'),(99,'s','What are the various techniques of knowledge representation in AI?','Knowledge representation techniques are given below:\n\nLogical Representation\nSemantic Network Representation\nFrame Representation\nProduction Rules'),(100,'s','Which programming language is not generally used in AI, and why?','Perl Programming language is not commonly used language for AI, as it is the scripting language.');

UNLOCK TABLES;

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

LOCK TABLES `botques` WRITE;

insert  into `botques`(`quesId`,`username`,`answer`,`botQues`) values (7,'s','yes',NULL);

UNLOCK TABLES;

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

LOCK TABLES `company` WRITE;

insert  into `company`(`id`,`fname`,`lname`,`mob`,`email`,`pass`,`role`) values (1,'abc','xyz','9856321470','a@gmail.com','a','Computer Science'),(2,'xyz','abc','0987654321','x@gmail.com','x','Electronics');

UNLOCK TABLES;

/*Table structure for table `deadline_over` */

DROP TABLE IF EXISTS `deadline_over`;

CREATE TABLE `deadline_over` (
  `jobId` int(255) NOT NULL auto_increment,
  `companyName` varchar(255) NOT NULL,
  `logo` longtext NOT NULL,
  `featureImage` longtext NOT NULL,
  `email` varchar(255) NOT NULL,
  `jobTitle` varchar(255) NOT NULL,
  `jobLoc` varchar(255) NOT NULL,
  `jobType` varchar(255) NOT NULL,
  `publishedOn` varchar(255) NOT NULL,
  `Vacancy` varchar(255) NOT NULL,
  `Experience` varchar(255) NOT NULL,
  `Salary` varchar(255) NOT NULL,
  `ApplicationDeadline` varchar(255) NOT NULL,
  `JobDescription` longtext NOT NULL,
  `Responsibilities` longtext NOT NULL,
  `Education_Experience` longtext NOT NULL,
  `OtherBenifits` longtext NOT NULL,
  `uname` varchar(255) NOT NULL,
  `branches` varchar(255) NOT NULL,
  `studentInfo` longtext NOT NULL,
  PRIMARY KEY  (`jobId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `deadline_over` */

LOCK TABLES `deadline_over` WRITE;

insert  into `deadline_over`(`jobId`,`companyName`,`logo`,`featureImage`,`email`,`jobTitle`,`jobLoc`,`jobType`,`publishedOn`,`Vacancy`,`Experience`,`Salary`,`ApplicationDeadline`,`JobDescription`,`Responsibilities`,`Education_Experience`,`OtherBenifits`,`uname`,`branches`,`studentInfo`) values (4,'Apple','../static/logo/apple-emblem.jpg','../static/company_img/106967633-1635506491361-gettyimages-1236193308-AA_29102021_503698.jpeg','karina_canvana@icloud.com','Flutter developer','New York','Part Time','2022-08-21','5','2-4','20LPA','2022-08-23','â€¢ Demonstrated ability to connect with customers through storytelling.\r\nâ€¢ Extraordinary presentation and public speaking skills with demonstrated ability to adapt to a complex audience with many learning styles.\r\nâ€¢ Deep and genuine connection to Appleâ€™s passion for delivering the best customer experience possible.','â€¢ Demonstrated ability to connect with customers through storytelling.\r\nâ€¢ Extraordinary presentation and public speaking skills with demonstrated ability to adapt to a complex audience with many learning styles.\r\nâ€¢ Deep and genuine connection to Appleâ€™s passion for delivering the best customer experience possible.','â€¢ Demonstrated ability to connect with customers through storytelling.\r\nâ€¢ Extraordinary presentation and public speaking skills with demonstrated ability to adapt to a complex audience with many learning styles.\r\nâ€¢ Deep and genuine connection to Appleâ€™s passion for delivering the best customer experience possible.','food','abc','Information Technology','[\'fname\', \'lname\', \'curntLoc\', \'achivmnt\', \'skil\', \'certif\', \'phnno\', \'actbacklog\']');

UNLOCK TABLES;

/*Table structure for table `jobinfo` */

DROP TABLE IF EXISTS `jobinfo`;

CREATE TABLE `jobinfo` (
  `jobId` int(255) NOT NULL auto_increment,
  `companyName` varchar(255) NOT NULL,
  `logo` longtext NOT NULL,
  `featureImage` longtext NOT NULL,
  `email` varchar(255) NOT NULL,
  `jobTitle` varchar(255) NOT NULL,
  `jobLoc` varchar(255) NOT NULL,
  `jobType` varchar(255) NOT NULL,
  `publishedOn` varchar(255) NOT NULL,
  `Vacancy` varchar(255) NOT NULL,
  `Experience` varchar(255) NOT NULL,
  `Salary` varchar(255) NOT NULL,
  `ApplicationDeadline` varchar(255) NOT NULL,
  `JobDescription` longtext NOT NULL,
  `Responsibilities` longtext NOT NULL,
  `Education_Experience` longtext NOT NULL,
  `OtherBenifits` longtext NOT NULL,
  `uname` varchar(255) NOT NULL,
  `branches` varchar(255) NOT NULL,
  `studentInfo` longtext,
  PRIMARY KEY  (`jobId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `jobinfo` */

LOCK TABLES `jobinfo` WRITE;

insert  into `jobinfo`(`jobId`,`companyName`,`logo`,`featureImage`,`email`,`jobTitle`,`jobLoc`,`jobType`,`publishedOn`,`Vacancy`,`Experience`,`Salary`,`ApplicationDeadline`,`JobDescription`,`Responsibilities`,`Education_Experience`,`OtherBenifits`,`uname`,`branches`,`studentInfo`) values (5,'Microsoft','../static/logo/aa1.jpg','../static/company_img/360_F_411584834_4I58F1DqKkz8eAp60QNl3O97ETjqMr5G.jpg','sd@gmail.com','software developer','Palo Alto','Full Time','2022-08-22','5','1-2','10LPA','2022-08-31','jadkfbkfbadbfjab','ajdhbad','akdbfkadbf','ajhbdfkabfk','abc','Computer science','[\'fname\', \'lname\', \'mothername\', \'achivmnt\', \'certif\', \'brnch\', \'percent10\']'),(6,'Apple','../static/logo/download_3.png','../static/company_img/download_3.png','madhavbansal9779@gmail.com','Flutter developer','San Francisco','Full Time','2022-08-23','10','0-1','50LPA','2022-08-24','Required Flutter Developer','Resposibilities','Work Ex','Travel','abc','Computer science','[\'fname\', \'lname\', \'skil\', \'rolno\', \'pEmail\']'),(7,'Mckinsey & Company','../static/logo/download_6.jpg','../static/company_img/download_6.jpg','madhavbansal9779@gmail.com','SDE','Anywhere','Part Time','2022-08-23','50','0-1','25LPA','2022-08-24','Dob Description','Software Development','NO','FOOD','abc','Electronics ','[\'fname\', \'lname\', \'fathername\', \'mothername\', \'curntLoc\', \'Hometown\', \'rolno\', \'pEmail\']');

UNLOCK TABLES;

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
  `achivmnt` varchar(255) NOT NULL default '',
  `skil` varchar(255) NOT NULL default '',
  `certif` varchar(255) NOT NULL default '',
  `cgpa1` varchar(255) NOT NULL default '',
  `cgpa2` varchar(255) NOT NULL,
  `cgpa3` varchar(255) NOT NULL,
  `cgpa4` varchar(255) NOT NULL,
  `cgpa5` varchar(255) NOT NULL,
  `cgpa6` varchar(255) NOT NULL,
  `cgpa7` varchar(255) NOT NULL,
  `cgpa8` varchar(255) NOT NULL,
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

LOCK TABLES `studentinfo` WRITE;

insert  into `studentinfo`(`studId`,`fname`,`lname`,`fathername`,`mothername`,`curntLoc`,`Hometown`,`achivmnt`,`skil`,`certif`,`cgpa1`,`cgpa2`,`cgpa3`,`cgpa4`,`cgpa5`,`cgpa6`,`cgpa7`,`cgpa8`,`clgname`,`rolno`,`cEmail`,`pEmail`,`phnno`,`brnch`,`degre`,`percent10`,`percent12`,`actbacklog`) values (1,'Madhav','Bansal','abc','xyz','Punjab','Amritsar','Consulted in the redesign of a companyâ€™s website, resulting in a 25% increase in traffic','Java,Python,React,Angular','Java,Python','6.5599999999999996','6.7999999999999998','7.2000000000000002','7.4000000000000004','7.5999999999999996','7.7999999999999998','8','0','XYZ collage of engineering','1T523641','b@gmail.com','madhav@gmail.com','9856321470','Information Technology','B.E','0.80000000000000004','0.84999999999999998','0'),(2,'Vedansh','Kapoor','abcd','jhi','Patiala','Ludhiana','ajhdba','ajdba','adjbakj','155','513','351','351','31','31','31','35135','akd','53533','s@gmail.com','vedansh@gmail.com','9856321452','Computer Science','B.E','0.90000000000000002','0.90000000000000002','1');

UNLOCK TABLES;

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

LOCK TABLES `userdetails` WRITE;

insert  into `userdetails`(`id`,`fname`,`lname`,`mob`,`email`,`pass`,`Department`) values (1,'Madhav','Bansal','9856321470','b@gmail.com','b','Information Technology'),(3,'Vedansh','Kapoor','9856321452','s@gmail.com','s','Computer Science');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
