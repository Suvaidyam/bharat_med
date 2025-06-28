<template>
	<div class="min-h-screen bg-gray-50">
		<!-- Header -->
		<div class="bg-white border-b border-gray-200 px-4 sm:px-6 lg:px-8 py-4">
			<div class="flex items-center gap-4">
				<button class="p-2 hover:bg-gray-100 rounded-lg transition-colors">
					<svg
						class="w-5 h-5 text-gray-600"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 19l-7-7 7-7"
						/>
					</svg>
				</button>
				<h1 class="text-xl font-semibold text-gray-900">Staff Attendance</h1>
			</div>
		</div>

		<div class="px-4 sm:px-6 lg:px-8 py-6">
			<!-- Stats Cards -->
			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
				<!-- Present Today -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-2">
						<h3 class="text-sm font-medium text-gray-600">Present Today</h3>
						<div class="p-2 bg-green-100 rounded-lg">
							<svg
								class="w-5 h-5 text-green-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
								/>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">{{ presentToday }}</div>
					<div class="flex items-center gap-2">
						<div class="flex-1 bg-gray-200 rounded-full h-2">
							<div
								class="bg-green-500 h-2 rounded-full"
								:style="{ width: `${(presentToday / totalStaff) * 100}%` }"
							></div>
						</div>
						<span class="text-xs text-green-600 font-medium">+2%</span>
					</div>
					<p class="text-xs text-gray-500 mt-1">Out of {{ totalStaff }} staff members</p>
				</div>

				<!-- Absent Today -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-2">
						<h3 class="text-sm font-medium text-gray-600">Absent Today</h3>
						<div class="p-2 bg-red-100 rounded-lg">
							<svg
								class="w-5 h-5 text-red-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
								/>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">{{ absentToday }}</div>
					<div class="flex items-center gap-2">
						<div class="flex-1 bg-gray-200 rounded-full h-2">
							<div
								class="bg-red-500 h-2 rounded-full"
								:style="{ width: `${(absentToday / totalStaff) * 100}%` }"
							></div>
						</div>
						<span class="text-xs text-red-600 font-medium">-1%</span>
					</div>
					<p class="text-xs text-gray-500 mt-1">Unplanned absences</p>
				</div>

				<!-- On Leave -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-2">
						<h3 class="text-sm font-medium text-gray-600">On Leave</h3>
						<div class="p-2 bg-blue-100 rounded-lg">
							<svg
								class="w-5 h-5 text-blue-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
								/>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">{{ onLeave }}</div>
					<div class="flex items-center gap-2">
						<div class="flex-1 bg-gray-200 rounded-full h-2">
							<div
								class="bg-blue-500 h-2 rounded-full"
								:style="{ width: `${(onLeave / totalStaff) * 100}%` }"
							></div>
						</div>
						<span class="text-xs text-gray-600 font-medium">0%</span>
					</div>
					<p class="text-xs text-gray-500 mt-1">Approved leave requests</p>
				</div>

				<!-- Late Arrivals -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-2">
						<h3 class="text-sm font-medium text-gray-600">Late Arrivals</h3>
						<div class="p-2 bg-yellow-100 rounded-lg">
							<svg
								class="w-5 h-5 text-yellow-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"
								/>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">{{ lateArrivals }}</div>
					<div class="flex items-center gap-2">
						<div class="flex-1 bg-gray-200 rounded-full h-2">
							<div
								class="bg-yellow-500 h-2 rounded-full"
								:style="{ width: `${(lateArrivals / totalStaff) * 100}%` }"
							></div>
						</div>
						<span class="text-xs text-yellow-600 font-medium">+1%</span>
					</div>
					<p class="text-xs text-gray-500 mt-1">More than 30 minutes late</p>
				</div>
			</div>

			<!-- Controls -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 mb-6">
				<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
					<div class="flex flex-col sm:flex-row gap-4">
						<!-- Search -->
						<div class="relative">
							<svg
								class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								/>
							</svg>
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search staff..."
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full sm:w-64"
							/>
						</div>

						<!-- Department Filter -->
						<select
							v-model="selectedDepartment"
							class="px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						>
							<option value="">All Departments</option>
							<option v-for="dept in departments" :key="dept" :value="dept">
								{{ dept }}
							</option>
						</select>

						<!-- Date Picker -->
						<div class="relative">
							<svg
								class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
								/>
							</svg>
							<input
								v-model="selectedDate"
								type="date"
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
					</div>

					<div class="flex gap-2">
						<button
							class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors flex items-center gap-2"
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
							Record Time
						</button>
						<button
							class="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors flex items-center gap-2"
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
								/>
							</svg>
							Export
						</button>
					</div>
				</div>

				<!-- Navigation Tabs -->
				<div class="flex flex-wrap gap-1 mt-4 border-b border-gray-200">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'flex items-center gap-2 px-4 py-2 text-sm font-medium border-b-2 transition-colors',
							activeTab === tab.id
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700',
						]"
					>
						<component :is="tab.icon" class="w-4 h-4" />
						{{ tab.label }}
					</button>
				</div>
			</div>

			<!-- Daily Attendance Record -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200">
				<div class="px-6 py-4 border-b border-gray-200">
					<div
						class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"
					>
						<h2 class="text-lg font-semibold text-gray-900">
							Daily Attendance Record
						</h2>
						<div class="flex gap-2">
							<button
								class="text-gray-600 hover:text-gray-900 px-3 py-1 text-sm font-medium flex items-center gap-2 transition-colors"
							>
								<svg
									class="w-4 h-4"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"
									/>
								</svg>
								Print
							</button>
							<button
								class="text-gray-600 hover:text-gray-900 px-3 py-1 text-sm font-medium flex items-center gap-2 transition-colors"
							>
								<svg
									class="w-4 h-4"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
									/>
								</svg>
								Export CSV
							</button>
						</div>
					</div>
				</div>

				<!-- Attendance Table -->
				<div class="overflow-x-auto">
					<table class="w-full">
						<thead class="bg-gray-50 border-b border-gray-200">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Staff
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden sm:table-cell"
								>
									Department
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden md:table-cell"
								>
									Role
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden lg:table-cell"
								>
									Check In
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden lg:table-cell"
								>
									Check Out
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden xl:table-cell"
								>
									Hours
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Actions
								</th>
							</tr>
						</thead>
						<tbody class="bg-white divide-y divide-gray-200">
							<tr
								v-for="record in filteredAttendance"
								:key="record.id"
								class="hover:bg-gray-50 transition-colors"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="flex items-center">
										<div
											class="h-10 w-10 rounded-full flex items-center justify-center text-white font-medium text-sm"
											:style="{ backgroundColor: record.avatarColor }"
										>
											{{ record.initials }}
										</div>
										<div class="ml-3">
											<div class="text-sm font-medium text-gray-900">
												{{ record.name }}
											</div>
											<div class="text-sm text-gray-500 sm:hidden">
												{{ record.department }}
											</div>
										</div>
									</div>
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 hidden sm:table-cell"
								>
									{{ record.department }}
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden md:table-cell"
								>
									{{ record.role }}
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden lg:table-cell"
								>
									<div class="flex items-center gap-2">
										<div class="w-2 h-2 bg-gray-300 rounded-full"></div>
										{{ record.checkIn }}
									</div>
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden lg:table-cell"
								>
									<div class="flex items-center gap-2">
										<div class="w-2 h-2 bg-gray-300 rounded-full"></div>
										{{ record.checkOut }}
									</div>
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 hidden xl:table-cell"
								>
									{{ record.hours }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										class="inline-flex px-2 py-1 text-xs font-medium rounded-full bg-green-100 text-green-800"
									>
										{{ record.status }}
									</span>
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
								>
									<button
										class="text-gray-400 hover:text-gray-600 transition-colors"
									>
										<svg
											class="w-5 h-5"
											fill="currentColor"
											viewBox="0 0 20 20"
										>
											<path
												d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
											/>
										</svg>
									</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Tab icons (using simple SVG strings for compatibility)
const UserIcon = {
	template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>`,
}
const CalendarIcon = {
	template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>`,
}
const ClockIcon = {
	template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>`,
}
const DocumentIcon = {
	template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>`,
}
const ChartIcon = {
	template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>`,
}

// Reactive data
const searchQuery = ref('')
const selectedDepartment = ref('')
const selectedDate = ref('2023-05-15')
const activeTab = ref('daily-attendance')

// Tabs configuration
const tabs = ref([
	{ id: 'daily-attendance', label: 'Daily Attendance', icon: UserIcon },
	{ id: 'calendar', label: 'Calendar View', icon: CalendarIcon },
	{ id: 'timesheets', label: 'Timesheets', icon: ClockIcon },
	{ id: 'leave-requests', label: 'Leave Requests', icon: DocumentIcon },
	{ id: 'reports', label: 'Reports', icon: ChartIcon },
])

// Sample attendance data
const attendanceData = ref([
	{
		id: 1,
		name: 'Dr. Sarah Johnson',
		department: 'Medical',
		role: 'Cardiologist',
		checkIn: '08:45 AM',
		checkOut: '05:30 PM',
		hours: '8.75',
		status: 'Present',
		initials: 'SJ',
		avatarColor: '#3B82F6',
	},
	{
		id: 2,
		name: 'Dr. Michael Chen',
		department: 'Medical',
		role: 'Neurologist',
		checkIn: '09:15 AM',
		checkOut: '06:00 PM',
		hours: '8.75',
		status: 'Present',
		initials: 'MC',
		avatarColor: '#8B5CF6',
	},
	{
		id: 3,
		name: 'Nurse Emma Wilson',
		department: 'Nursing',
		role: 'Head Nurse',
		checkIn: '08:00 AM',
		checkOut: '04:30 PM',
		hours: '8.5',
		status: 'Present',
		initials: 'EW',
		avatarColor: '#EF4444',
	},
	{
		id: 4,
		name: 'James Rodriguez',
		department: 'Laboratory',
		role: 'Lab Technician',
		checkIn: '08:30 AM',
		checkOut: '05:00 PM',
		hours: '8.5',
		status: 'Present',
		initials: 'JR',
		avatarColor: '#F59E0B',
	},
	{
		id: 5,
		name: 'Lisa Thompson',
		department: 'Administration',
		role: 'Receptionist',
		checkIn: '08:55 AM',
		checkOut: '05:15 PM',
		hours: '8.33',
		status: 'Present',
		initials: 'LT',
		avatarColor: '#10B981',
	},
])

// Computed properties
const departments = computed(() => {
	const depts = [...new Set(attendanceData.value.map((record) => record.department))]
	return depts.sort()
})

const filteredAttendance = computed(() => {
	let filtered = attendanceData.value

	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(record) =>
				record.name.toLowerCase().includes(query) ||
				record.department.toLowerCase().includes(query) ||
				record.role.toLowerCase().includes(query),
		)
	}

	if (selectedDepartment.value) {
		filtered = filtered.filter((record) => record.department === selectedDepartment.value)
	}

	return filtered
})

// Stats
const totalStaff = computed(() => 8)
const presentToday = computed(() => 5)
const absentToday = computed(() => 1)
const onLeave = computed(() => 1)
const lateArrivals = computed(() => 1)
</script>
