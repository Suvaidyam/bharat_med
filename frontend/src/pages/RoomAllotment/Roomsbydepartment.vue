<template>
	<div class="p-6">
		<!-- Header -->
		<div class="flex justify-between items-center mb-4">
			<h1 class="text-2xl font-semibold">Rooms by Department</h1>
			<button
				class="flex items-center bg-black text-white px-4 py-2 rounded hover:bg-gray-800"
			>
				<span class="text-xl mr-2">+</span> Add New Room
			</button>
		</div>

		<!-- Department Stats -->
		<div class="grid md:grid-cols-3 gap-4 mb-6">
			<div v-for="dept in departments" :key="dept.name" class="bg-white border rounded p-4">
				<h2 class="text-lg font-medium">{{ dept.name }}</h2>
				<p class="text-3xl font-bold my-2">{{ dept.total }}</p>
				<div class="text-sm space-y-1">
					<p class="text-green-600">🟢 Available: {{ dept.available }}</p>
					<p class="text-red-600">🔴 Occupied: {{ dept.occupied }}</p>
				</div>
			</div>
		</div>

		<!-- Tabs -->
		<div class="flex flex-wrap items-center gap-2 mb-4">
			<button
				v-for="tab in tabs"
				:key="tab"
				@click="selectedTab = tab"
				:class="[
					'px-4 py-1 rounded-full text-sm',
					selectedTab === tab
						? 'bg-black text-white'
						: 'bg-gray-100 hover:bg-gray-200 text-gray-700',
				]"
			>
				{{ tab }}
			</button>
		</div>

		<!-- Filters -->
		<div class="flex flex-wrap justify-between items-center mb-4 gap-2">
			<input type="text" placeholder="Search rooms..." class="input max-w-xs" />

			<div class="flex gap-2">
				<select class="input">
					<option>All Statuses</option>
				</select>
				<select class="input">
					<option>All Types</option>
				</select>
			</div>
		</div>

		<!-- Table -->
		<div class="overflow-auto">
			<table class="min-w-full table-auto text-sm">
				<thead class="text-left bg-gray-50">
					<tr class="border-b">
						<th class="p-3">Room Number</th>
						<th class="p-3">Room Type</th>
						<th class="p-3">Status</th>
						<th class="p-3">Patient</th>
						<th class="p-3">Doctor</th>
						<th class="p-3 text-right">Actions</th>
					</tr>
				</thead>
				<tbody>
					<tr
						v-for="room in filteredRooms"
						:key="room.number"
						class="border-b hover:bg-gray-50"
					>
						<td class="p-3">{{ room.number }}</td>
						<td class="p-3">{{ room.type }}</td>
						<td class="p-3">
							<span
								:class="[
									'px-2 py-1 text-xs rounded-full font-medium',
									room.status === 'Available'
										? 'bg-green-100 text-green-700'
										: 'bg-red-100 text-red-700',
								]"
							>
								{{ room.status }}
							</span>
						</td>
						<td class="p-3">{{ room.patient || '—' }}</td>
						<td class="p-3">{{ room.doctor || '—' }}</td>
						<td class="p-3 text-right">
							<button class="text-gray-500 hover:text-black">⋮</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

const departments = [
	{ name: 'Cardiology', total: 25, available: 7, occupied: 18 },
	{ name: 'Orthopedics', total: 20, available: 5, occupied: 15 },
	{ name: 'Neurology', total: 15, available: 5, occupied: 10 },
]

const tabs = [
	'Cardiology',
	'Orthopedics',
	'Neurology',
	'Pulmonology',
	'Gastroenterology',
	'Pediatrics',
]
const selectedTab = ref('Cardiology')

const rooms = ref([
	{
		number: 101,
		type: 'Private',
		status: 'Occupied',
		patient: 'John Smith',
		doctor: 'Dr. Emily Chen',
		department: 'Cardiology',
	},
	{
		number: 102,
		type: 'Private',
		status: 'Available',
		patient: '',
		doctor: '',
		department: 'Cardiology',
	},
	{
		number: 103,
		type: 'Semi-Private',
		status: 'Occupied',
		patient: 'Maria Garcia',
		doctor: 'Dr. James Wilson',
		department: 'Cardiology',
	},
	{
		number: 104,
		type: 'Semi-Private',
		status: 'Occupied',
		patient: 'Robert Davis',
		doctor: 'Dr. Lisa Wong',
		department: 'Cardiology',
	},
	{
		number: 105,
		type: 'General',
		status: 'Available',
		patient: '',
		doctor: '',
		department: 'Cardiology',
	},
])

const filteredRooms = computed(() =>
	rooms.value.filter((room) => room.department === selectedTab.value),
)
</script>
