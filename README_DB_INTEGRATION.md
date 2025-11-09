VIDYAMITRA DB Integration Notes
------------------------------
I added a MongoDB connector file at: backend_utils/db.js
How to use:
1. Install mongoose: npm install mongoose dotenv
2. Set MONGODB_URI in environment or create .env in project root.
3. In your main server file (e.g., index.js) add:
   const connectDB = require('./backend_utils/db.js');
   connectDB();
I did NOT change app flow since no server file was auto-detected.
