##For Team Members

### Fenthon (Recovery Engine):
Your integration points are in `app/integration/`:
- `recovery_engine.py` - Calculate recovery scores
- `recommendation_rules.py` - Generate workout recommendations  
- `progression_tracker.py` - Track weight progression

See `app/api/routes/recovery.py` for how they're called.

### Andrew (Frontend):
**Live API:** https://equilibria-backend-g5oa.onrender.com
**Documentation:** https://equilibria-backend-g5oa.onrender.com/docs

Key endpoints:
- POST `/api/v1/auth/register` - Register user
- POST `/api/v1/auth/login` - Login (returns JWT)
- POST `/api/v1/recovery/log` - Log recovery data
- GET `/api/v1/recovery/latest` - Get today's recommendation

### Ian (Deployment):
Already deployed to Render! Can also deploy to:
- Railway.app
- Fly.io  
- AWS/Azure/GCP

### Kadeem (Testing):
- Interactive tests: https://equilibria-backend.onrender.com/docs
- Postman collection: `equilibria_api.json`
- All endpoints have validation and error handling
