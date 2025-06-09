<template>
	<div class="p-6 bg-white min-h-screen">
		<!-- Header -->
		<div class="flex items-center mb-4 space-x-3">
			<button class="text-2xl font-bold">&larr;</button>
			<div>
				<h1 class="text-2xl font-semibold">Appointment Calendar</h1>
				<p class="text-gray-500 text-sm">View and manage appointments in calendar view.</p>
			</div>
		</div>

		<!-- Calendar Toolbar -->
		<div class="bg-white rounded-lg shadow p-4">
			<div class="flex flex-wrap items-center justify-between mb-4">
				<!-- View Selector -->
				<div class="space-x-2 mb-2 sm:mb-0">
					<button class="px-3 py-1 rounded border border-gray-300 bg-gray-100 text-sm">
						Day
					</button>
					<button class="px-3 py-1 rounded border border-gray-300 text-sm">Week</button>
					<button class="px-3 py-1 rounded border border-gray-300 text-sm">Month</button>
				</div>

				<!-- Date Controls -->
				<div class="flex items-center space-x-2 mb-2 sm:mb-0">
					<button class="px-3 py-1 border border-gray-300 rounded">Today</button>
					<button class="px-2 py-1 border border-gray-300 rounded">&lt;</button>
					<button class="px-2 py-1 border border-gray-300 rounded">&gt;</button>
					<span class="font-semibold">June 9, 2025</span>
				</div>

				<!-- Filters & New -->
				<div class="flex items-center space-x-2">
					<select class="border border-gray-300 rounded px-3 py-1 text-sm">
						<option>All Doctors</option>
					</select>
					<button class="px-4 py-1 bg-black text-white rounded text-sm">+ New</button>
				</div>
			</div>

			<!-- Calendar Grid -->
			<div>
				<div v-for="hour in timeSlots" :key="hour.time" class="border-t py-4">
					<div class="flex items-start space-x-4">
						<div class="w-20 text-sm text-gray-500">{{ hour.time }}</div>
						<div class="flex-1 space-y-3">
							<div
								v-for="appt in hour.appointments"
								:key="appt.name"
								:class="['rounded-lg p-4 shadow-sm border', appt.bgColor]"
							>
								<div class="flex items-center justify-between">
									<div class="flex items-center space-x-2">
										<img :src="appt.avatar" class="w-6 h-6 rounded-full" />
										<span class="font-semibold">{{ appt.name }}</span>
									</div>
									<span
										:class="[
											'text-xs px-2 py-0.5 rounded-full font-medium',
											appt.statusColor,
										]"
									>
										{{ appt.status }}
									</span>
								</div>
								<div class="text-sm text-gray-600">{{ appt.time }}</div>
								<div class="text-sm text-gray-500">{{ appt.doctor }}</div>
								<div class="text-sm text-gray-400 italic">{{ appt.type }}</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
const timeSlots = [
	{
		time: '08:00 AM',
		appointments: [],
	},
	{
		time: '09:00 AM',
		appointments: [],
	},
	{
		time: '10:00 AM',
		appointments: [
			{
				name: 'John Smith',
				avatar: 'https://i.pravatar.cc/30?u=john',
				time: '10:00 AM - 10:30 AM',
				doctor: 'Dr. Sarah Johnson',
				type: 'Check-up',
				status: 'Confirmed',
				statusColor: 'text-blue-700 bg-blue-100',
				bgColor: 'bg-blue-50 border-blue-200',
			},
		],
	},
	{
		time: '11:00 AM',
		appointments: [
			{
				name: 'Emily Davis',
				avatar: 'https://i.pravatar.cc/30?u=emily',
				time: '11:30 AM - 12:15 PM',
				doctor: 'Dr. Michael Chen',
				type: 'Consultation',
				status: 'In Progress',
				statusColor: 'text-orange-700 bg-orange-100',
				bgColor: 'bg-orange-50 border-orange-200',
			},
		],
	},
	{
		time: '12:00 PM',
		appointments: [],
	},
	{
		time: '01:00 PM',
		appointments: [],
	},
]
</script>
