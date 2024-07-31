#!/usr/bin/node
/* 6. Retrieve and process API data. */

const request = require('request');
const apiUrl = process.argv[2];

const userIds = [];
const userTasks = {};

request(apiUrl, (error, response, data) => {
  if (error) {
    throw error;
  }
  const tasks = JSON.parse(data);
  tasks.forEach(task => {
    if (task.completed) {
      userIds.push(task.userId);
    }
  });
  const uniqueIds = new Set(userIds);
  uniqueIds.forEach(id => {
    userTasks[id] = 0;
  });
  tasks.forEach(task => {
    if (task.completed) {
      userTasks[task.userId]++;
    }
  });
  console.log(userTasks);
});
