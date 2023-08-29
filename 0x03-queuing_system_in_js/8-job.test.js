import { expect } from 'chai';
import kue from 'kue';
import { createPushNotificationsJobs } from './8-job'; // Update with the correct path

describe('createPushNotificationsJobs', function () {
  let queue;

  before(function () {
    // Create a Kue queue
    queue = kue.createQueue();
  });

  beforeEach(function () {
    // Enable test mode and clear the queue before each test
    queue.testMode.enter();
    queue.testMode.clear();
  });

  afterEach(function () {
    // Exit test mode and clear the queue after each test
    queue.testMode.exit();
    queue.testMode.clear();
  });

  after(function () {
    // Shutdown the Kue queue after all tests are done
    queue.shutdown(1000, function () {
      console.log('Queue has been shut down.');
    });
  });

  it('displays an error message if jobs is not an array', function () {
    // Call the createPushNotificationsJobs function with non-array input
    const nonArrayInput = 'not an array';
    createPushNotificationsJobs(queue, nonArrayInput);

    // Check if the queue is empty
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('creates two new jobs in the queue', function () {
    // Call the createPushNotificationsJobs function with an array of job data
    const jobData = [{ message: 'Message 1' }, { message: 'Message 2' }];
    createPushNotificationsJobs(queue, jobData);

    // Check if the queue contains two jobs
    expect(queue.testMode.jobs.length).to.equal(2);

    // Optionally, you can perform additional assertions on the created jobs
    const jobs = queue.testMode.jobs;
    expect(jobs[0].data.message).to.equal('Message 1');
    expect(jobs[1].data.message).to.equal('Message 2');
  });

  // Add more test cases as needed
});
