# Reconstruct Itinerary

## Link

https://leetcode.com/problems/reconstruct-itinerary/description/

## Where

Leetcode

## Difficulty

Hard

## Description

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

## Solution Main Idea

Create adj list, modify list as you DFS to ensure you only traverse an edge once. Restore that edge once youre done DFS'ing.
Sort the neighbours lexicalgraphically. Return first result that uses all edges.
