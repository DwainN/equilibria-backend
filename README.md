##For Team Members

Fenthon (Recovery Engine):
Your integration points are ready in app/integration/:
- recovery_engine.py - Recovery score calculation (currently has placeholder)
- recommendation_rules.py - Workout intensity rules (currently has placeholder)
- progression_tracker.py - Weight progression tracking

To integrate:
1. git clone https://github.com/DwainN/equilibria-backend.git
2. Add your modules to app/integration/
3. See app/api/routes/recovery.py for how they're called
4. Push to a new branch and I'll merge it

Andrew (Mobile Frontend):
API Base URL: https://YOUR-URL.onrender.com
Full API Documentation: https://YOUR-URL.onrender.com/docs

Key Endpoints:
- POST /api/v1/auth/register - Register new user
- POST /api/v1/auth/login - Login (returns JWT token)
- GET /api/v1/auth/me - Get current user
- POST /api/v1/recovery/log - Log daily recovery data
- GET /api/v1/recovery/latest - Get today's score & recommendation
- POST /api/v1/wearables/sync - Sync wearable data
- POST /api/v1/workouts/ - Create workout plan
- POST /api/v1/workouts/sessions - Log workout session

Authentication: Include JWT token in headers:
Authorization: Bearer <token>

Ian (Deployment):
Already deployed to Render! 
- Backend: Live and running
- Database: PostgreSQL on Render
- Cache: Redis on Upstash
- Containers: Docker + Docker Compose

If you need to redeploy elsewhere, everything is containerized and ready.

Kadeem (Testing):
Interactive API Testing: https://YOUR-URL.onrender.com/docs
- Click any endpoint → "Try it out" → Test directly in browser
- Postman collection in repo: equilibria_api.json
- All endpoints have validation and detailed error messages

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 To Run Locally (For Development):
1. Clone: git clone https://github.com/DwainN/equilibria-backend.git
2. Install Docker Desktop: https://docker.com
3. Run: docker-compose up --build
4. Access: http://localhost:8000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ Tech Stack:
- Backend: FastAPI (Python 3.11)
- Database: PostgreSQL 15
- Cache/Queue: Redis + Celery
- Authentication: JWT (JSON Web Tokens)
- Deployment: Docker + Render
- Data Processing: NumPy, Pandas, SciPy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Questions or issues? Let me know!

All my deliverables are complete and ready for integration. 🚀
