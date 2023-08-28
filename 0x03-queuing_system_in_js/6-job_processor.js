import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Create the sendNotification function
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the push_notification_code queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done(); // Indicate job completion
});

// Start processing jobs
queue.active(); // Start the queue processing

// Log when the processor is ready
console.log('Job processor is ready and listening for new jobs.');
