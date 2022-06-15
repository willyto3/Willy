import mongoose from "mongoose";

try {
  await mongoose.connect(process.env.CONNECTION_DB, { dbName: "OrlandoKorzo" });

  console.log("Connected to MongoDB");
} catch (error) {
  console.log("Connection Error");
}
