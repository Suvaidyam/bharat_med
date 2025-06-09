<template>
	<div class="p-6 bg-white min-h-screen">
		<!-- Page Title -->
		<h1 class="text-2xl font-bold mb-2">Appointment Dashboard</h1>
		<p class="text-sm text-gray-500 mb-6">Manage appointments and requests.</p>

		<!-- Calendar Section -->
		<section class="bg-white p-4 rounded-lg shadow mb-10">
			<div class="flex justify-between items-center mb-4">
				<h2 class="text-lg font-semibold">Calendar</h2>
				<div class="flex items-center gap-2">
					<button class="px-3 py-1 border rounded">Today</button>
					<input type="date" class="border rounded px-2 py-1 text-sm" />
				</div>
			</div>

			<!-- Sample Appointments (use a calendar library for real UI) -->
			<div class="space-y-3">
				<div class="border-l-4 border-blue-300 bg-blue-50 p-3 rounded shadow-sm">
					<div class="flex justify-between">
						<div>
							<p class="font-medium text-sm">John Smith</p>
							<p class="text-xs text-gray-500">
								10:00 AM – 10:30 AM • Dr. Sarah Johnson
							</p>
						</div>
						<div class="text-xs text-blue-600 bg-blue-100 px-2 py-0.5 rounded-full">
							Confirmed
						</div>
					</div>
				</div>
				<div class="border-l-4 border-yellow-300 bg-yellow-50 p-3 rounded shadow-sm">
					<div class="flex justify-between">
						<div>
							<p class="font-medium text-sm">Emily Davis</p>
							<p class="text-xs text-gray-500">
								11:30 AM – 12:15 PM • Dr. Michael Chen
							</p>
						</div>
						<div
							class="text-xs text-yellow-700 bg-yellow-100 px-2 py-0.5 rounded-full"
						>
							In Progress
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Appointment Requests Section -->
		<section class="bg-white p-4 rounded-lg shadow">
			<div class="flex justify-between items-center mb-4">
				<h2 class="text-lg font-semibold">Appointment Requests</h2>
				<input
					type="text"
					placeholder="Search requests..."
					class="border px-2 py-1 text-sm rounded"
				/>
			</div>

			<!-- Tabs -->
			<div class="flex space-x-2 border-b mb-4">
				<button class="px-3 py-2 text-sm font-medium border-b-2 border-black">
					Pending
				</button>
				<button class="px-3 py-2 text-sm text-gray-500 hover:text-black">Approved</button>
				<button class="px-3 py-2 text-sm text-gray-500 hover:text-black">Rejected</button>
			</div>

			<!-- Request Table -->
			<div class="overflow-x-auto">
				<table class="min-w-full text-sm">
					<thead>
						<tr class="text-left text-gray-600 border-b">
							<th class="py-2">Patient</th>
							<th class="py-2">Doctor</th>
							<th class="py-2">Preferred Date</th>
							<th class="py-2">Type</th>
							<th class="py-2">Urgency</th>
							<th class="py-2 text-right">Actions</th>
						</tr>
					</thead>
					<tbody>
						<tr class="border-b hover:bg-gray-50">
							<td class="py-2">John Smith</td>
							<td class="py-2">Dr. Sarah Johnson</td>
							<td class="py-2">2023-07-25 (Morning)</td>
							<td class="py-2">Check-up</td>
							<td class="py-2">
								<span
									class="px-2 py-0.5 text-xs rounded-full bg-blue-100 text-blue-700"
									>Normal</span
								>
							</td>
							<td class="py-2 text-right">
								<button class="text-gray-500 hover:text-black">•••</button>
							</td>
						</tr>
						<tr class="border-b hover:bg-gray-50">
							<td class="py-2">Emily Davis</td>
							<td class="py-2">Any cardiologist</td>
							<td class="py-2">2023-07-28 (Afternoon)</td>
							<td class="py-2">Consultation</td>
							<td class="py-2">
								<span
									class="px-2 py-0.5 text-xs rounded-full bg-red-100 text-red-700"
									>High</span
								>
							</td>
							<td class="py-2 text-right">
								<button class="text-gray-500 hover:text-black">•••</button>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</section>
	</div>
</template>
