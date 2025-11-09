# TellmeMore - AI-Powered Mock Interview Platform

A comprehensive Django-based mock interview system that uses Google's Gemini AI to provide personalized interview experiences with real-time feedback and analytics.

---

##  Problem We Are Solving
Many students and job seekers practice interviews, but:
- They **don’t receive personalized feedback**
- They **repeat the same mistakes**
- They **lack confidence while speaking**
- They **don’t get real interview-like experience**

**TellmeMore** solves this by using **Google Gemini AI** to:
- Generate interview questions based on user profile and selected role
- Evaluate voice/text responses in real-time
- Provide improvement suggestions and confidence scoring

---

##  Core Features

### 🎙 AI-Powered Interview Modes
- **Technical Interviews** (Based on programming languages & domain)
- **HR / Behavioral Interviews**
- **Group Discussions & Presentation Practice**
- **Communication Skills Practice**
- **Custom Question Sets**

###  Smart AI Feedback
- Gemini AI evaluates your tone, clarity, answer depth, and confidence
- Gives **instant improvement suggestions**
- Generates **follow-up questions** based on responses

###  Analytics Dashboard
- Performance trend charts
- Average response time & confidence score
- Strength & improvement insights
- Session history with downloadable reports

###  Professional UI Experience
- Modern **dark professional theme**
- Clean dashboard with user profile & progress charts
- Responsive design for mobile & laptop

---

##  Tech Stack

- **Backend**: Django 5.2.1
- **Frontend**: Tailwind CSS, Vanilla JavaScript
- **AI Integration**: Google Gemini AI API
- **Database**: SQLite (development) / PostgreSQL (production)
- **Charts**: Chart.js
- **Icons**: Lucide Icons

##  Installation

### Prerequisites
- Python 3.8+
- pip
- Git

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TellmeMore
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` to access the application.

##  Configuration

### Gemini AI Setup

1. **Get API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file:
     ```
     GEMINI_API_KEY=your-api-key-here
     ```

2. **API Features**
   - Dynamic question generation based on user profile
   - Real-time answer evaluation
   - Personalized feedback and improvement suggestions
   - Contextual follow-up questions

### Database Models

#### Core Models
- **InterviewDetails**: User interview profiles and preferences
- **InterviewSession**: Individual interview sessions with timing and scores
- **SessionQuestion**: Individual questions and responses within sessions
- **SessionAnalytics**: Detailed performance metrics and recommendations

#### Practice Models
- **PresentationPractice**: Presentation-specific sessions
- **CommunicationPractice**: Language and communication skill development
- **CustomQuestionSet**: User-created custom question collections

##  Usage Guide

### Getting Started

1. **Registration & Profile Setup**
   - Create account and complete profile
   - Upload resume (optional) for personalized questions
   - Set skills, experience level, and target role

2. **Choose Interview Type**
   - Navigate to Categories page
   - Select from available interview types
   - Configure difficulty and time settings

3. **Start Interview Session**
   - AI generates contextual questions
   - Respond via text or voice input
   - Receive real-time feedback
   - Track performance metrics

4. **Review Analytics**
   - View performance trends over time
   - Identify strengths and improvement areas
   - Get AI-powered recommendations

### Key Features Usage

#### AI Interview Session
- **Start Session**: Click "Start Session" to begin
- **Answer Questions**: Use text input or voice recording
- **Real-time Timer**: Track answer time per question
- **Pause/Resume**: Manage session flow as needed
- **End Session**: Complete interview for detailed feedback

#### Analytics Dashboard
- **Performance Metrics**: Track scores, timing, and improvement
- **Visual Charts**: See progress trends and skill breakdowns
- **Session History**: Review past interviews and results
- **Export Reports**: Download detailed performance reports

##  API Endpoints

### Frontend-Backend Integration
- `POST /dashboard/generate_question/` - AI question generation
- `POST /dashboard/evaluate_answer/` - AI answer evaluation
- `GET /dashboard/analytics/` - Performance analytics data

### Session Management
- Auto-save session progress
- Real-time score calculation
- Contextual question adaptation
- Performance trend analysis 

##  UI/UX Features

### Design System
- **Color Palette**: Professional dark theme with gradient accents
  - Primary: `#190019` (Deep Purple)
  - Secondary: `#2B124C` (Dark Purple)
  - Accent: `#854F6C` (Medium Purple)
  - Highlight: `#DFB6B2` (Mauve)
  - Light: `#FBE4D8` (Cream)

### Interactive Elements
- **Hover Effects**: Smooth transitions and shadow effects
- **Loading States**: Professional spinners and animations
- **Responsive Layout**: Mobile-first design approach
- **Accessibility**: Keyboard navigation and screen reader support

### Professional Components
- **Modern Cards**: Gradient backgrounds with hover animations
- **Progress Indicators**: Visual feedback for completion status
- **Interactive Charts**: Real-time data visualization
- **Professional Forms**: Consistent styling with focus states

##  Analytics & Reporting

### Performance Metrics
- **Overall Confidence Score**: AI-calculated performance rating
- **Response Time Analysis**: Average, longest, shortest response times
- **Skill Assessment**: Category-specific performance breakdown
- **Improvement Tracking**: Progress over time visualization

### AI-Powered Insights
- **Strengths Identification**: Areas of strong performance
- **Improvement Recommendations**: Targeted skill development suggestions
- **Practice Topics**: AI-suggested areas for focused practice
- **Difficulty Adjustments**: Dynamic difficulty recommendations

##  Production Deployment

### Environment Setup
1. Set `DEBUG=False` in production
2. Configure proper `ALLOWED_HOSTS`
3. Use PostgreSQL for production database
4. Set up static file serving (WhiteNoise or CDN)
5. Configure email backend for notifications

### Security Considerations
- Enable SSL/HTTPS in production
- Set secure cookie flags
- Configure CSRF protection
- Implement rate limiting for API endpoints
- Regular security updates for dependencies

##  Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Support & Contact

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Documentation**: Comprehensive guides in the `/docs` directory
- **Community**: Join our Discord for real-time support

---

**TellmeMore** - Empowering your interview success with AI-driven practice and feedback. 
